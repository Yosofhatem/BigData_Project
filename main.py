import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, when, count, avg,max,min
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, BooleanType, FloatType,TimestampType
from mysql_handler import MySQLHandler
import mysql.connector


# Create Spark session
spark = SparkSession.builder\
    .appName("CrimeAnalysis")\
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.4")\
    .config("spark.jars","c:\spark\jars\mysql-connection-j-8.2.0.jar") \
    .getOrCreate()
#.config("spark.driver.extraClassPath", "C:\spark\jars\mysql-connector-j-8.2.0.jar") \
#.config("spark.executor.extraClassPath", "C:\spark\jars\mysql-connector-j-8.2.0.jar") \

    
# Create Kafka DStream
kafka_df = spark.readStream.format("kafka")\
    .option("kafka.bootstrap.servers", "localhost:9092")\
    .option("subscribe", "Crimetopic")\
    .option("startingOffsets", "earliest")\
    .load()

# Define the schema for the JSON data
json_schema = StructType([
    StructField("CrimeType", StringType(), True),
    StructField("Location", StringType(), True),
    StructField("Date", TimestampType(), True),
    StructField("Time", StringType(), True),
    StructField("ArrestedParty", StructType([
        StructField("Name", StringType(), True),
        StructField("Age", IntegerType(), True),
        StructField("Gender", StringType(), True),
        StructField("Address", StringType(), True),
        StructField("Charges", StringType(), True),
        StructField("ArrestLocation", StringType(), True)
    ]), True),
    StructField("VictimInfo", StructType([
        StructField("VictimName", StringType(), True),
         StructField("VictimAge", IntegerType(), True),
        StructField("VictimGender", StringType(), True),
        StructField("VictimAddress", StringType(), True),
        StructField("InjuryType", StringType(), True),
        StructField("ImpactOnVictim", StringType(), True)
    ]), True),
    StructField("OtherFactors", StructType([
        StructField("WeatherConditions", StringType(), True),
        StructField("Witnesses", BooleanType(), True),
        StructField("EvidenceCollected", BooleanType(), True),
        StructField("PoliceResponseTime", FloatType(), True)
    ]), True)
])


# Parse JSON data to DataFrame
parsed_df = kafka_df.selectExpr("CAST(value AS STRING)")\
    .select(from_json("value", json_schema).alias("data"))\
    .select("data.*")

# Create an instance of the MySQLHandler class


# Analysis based on crime_data_analysis
crime_data_analysis = parsed_df.groupBy("CrimeType","Location", "Date").agg(
    count("CrimeType").alias("CrimeCount") 
)

# Save crime_data_analysis to MySQLc
crime_data_analysis.writeStream \
    .outputMode("complete") \
    .foreachBatch(lambda batch_df, batch_id: MySQLHandler.save_to_mysql(batch_df, "crime_data_analysis")) \
    .start()
    
    
# Analysis based on demographic_data_analysis
demographic_data_analysis = parsed_df.groupBy("ArrestedParty.Name","VictimInfo.VictimName", "ArrestedParty.ArrestLocation","VictimInfo.InjuryType").agg(
    count("CrimeType").alias("CrimeCount") 
     

)

# Save demographic analysis to MySQLc
demographic_data_analysis.writeStream \
    .outputMode("complete") \
    .foreachBatch(lambda batch_df, batch_id: MySQLHandler.save_to_mysql(batch_df, "demographic_data_analysis")) \
    .start()
    

 
 # Analysis based on Arrested_data_analysis
Arrested_data_analysis = parsed_df.groupBy("ArrestedParty.Charges","ArrestedParty.Gender", "ArrestedParty.Address","ArrestedParty.Age").agg(
    count("ArrestedParty.Charges").alias("TotalCharges"),
    avg("ArrestedParty.Age").alias("AvgAgeArrested"),
    
)
Arrested_data_analysis.writeStream \
    .outputMode("complete") \
    .foreachBatch(lambda batch_df, batch_id: MySQLHandler.save_to_mysql(batch_df, "Arrested_data_analysis")) \
    .start()



# Witnesses and witness_evidence_analysis
witness_evidence_analysis = parsed_df.groupBy(
    "Location", 
    "OtherFactors.Witnesses",
    "OtherFactors.EvidenceCollected"
).agg(
    count("CrimeType").alias("TotalCrimes")
)
# Save witness_evidence_analysis to MySQL
witness_evidence_analysis.writeStream \
    .outputMode("complete") \
    .foreachBatch(lambda batch_df, batch_id: MySQLHandler.save_to_mysql(batch_df, "witness_evidence_analysis")) \
    .start()
    
    
    
# Victim Information Analysis
victim_analysis = parsed_df.groupBy(
    "VictimInfo.VictimAge", 
    "VictimInfo.VictimGender", 
    "VictimInfo.InjuryType"
).agg(
    count("CrimeType").alias("TotalCrimes"),
    avg("OtherFactors.PoliceResponseTime").alias("AvgPoliceResponseTime")
)  
# Save victim_analysis to MySQL
victim_analysis.writeStream \
    .outputMode("complete") \
    .foreachBatch(lambda batch_df, batch_id: MySQLHandler.save_to_mysql(batch_df, "victim_analysis")) \
    .start()  
    
# Police Response Time Analysis
Police_response_time_analysis = parsed_df.groupBy("OtherFactors.WeatherConditions").agg(
    count("CrimeType").alias("TotalCrimes"),
    avg("OtherFactors.PoliceResponseTime").alias("AvgPoliceResponseTime")
)    


# Save Police_response_time_analysis to MySQL
Police_response_time_analysis.writeStream \
    .outputMode("complete") \
    .foreachBatch(lambda batch_df, batch_id: MySQLHandler.save_to_mysql(batch_df, "Police_response_time_analysis")) \
    .start()  
    
        
 
# Wait for the termination of the queries
spark.streams.awaitAnyTermination()