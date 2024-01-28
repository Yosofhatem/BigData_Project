import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, when, count, avg
from pyspark.sql.types import StructType, StructField, StringType, IntegerType,TimestampType ,BooleanType, FloatType,TimestampType

# Create Spark session
spark = SparkSession.builder\
    .appName("CrimeAnalysis")\
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.4")\
    .getOrCreate()

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
 
# Analysis based on crime_data_analysis
crime_data_analysis = parsed_df.groupBy("CrimeType","Location", "Date").agg(
    count("CrimeType").alias("CrimeCount") 
)
 
# Display behavior analysis
crime_behavior = crime_data_analysis.writeStream\
    .outputMode("complete")\
    .format("console")\
    .start()
    
crime_behavior.awaitTermination()


demographic_data_analysis = parsed_df.groupBy("ArrestedParty.Name","VictimInfo.VictimName", "ArrestedParty.ArrestLocation","VictimInfo.InjuryType").agg(
    count("CrimeType").alias("CrimeCount") 
     

)


# Display behavior analysis
demographic_behavior = demographic_data_analysis.writeStream\
    .outputMode("complete")\
    .format("console")\
    .start()
    
demographic_behavior.awaitTermination()


 # Analysis based on Arrested_data_analysis
Arrested_data_analysis = parsed_df.groupBy("ArrestedParty.Charges","ArrestedParty.Gender", "ArrestedParty.Address","ArrestedParty.Age").agg(
    count("ArrestedParty.Charges").alias("TotalCharges"),
    avg("ArrestedParty.Age").alias("AvgAgeArrested"),
    
)



# Display behavior analysis
Arrested_behavior = Arrested_data_analysis.writeStream\
    .outputMode("complete")\
    .format("console")\
    .start()
    
Arrested_behavior.awaitTermination()



# Witnesses and witness_evidence_analysis
witness_evidence_analysis = parsed_df.groupBy(
    "Location", 
    "OtherFactors.Witnesses",
    "OtherFactors.EvidenceCollected"
).agg(
    count("CrimeType").alias("TotalCrimes")
)


# Display behavior analysis
witness_evidence_behavior = witness_evidence_analysis.writeStream\
    .outputMode("complete")\
    .format("console")\
    .start()
    
witness_evidence_behavior.awaitTermination()


# Victim Information Analysis
victim_analysis = parsed_df.groupBy(
    "VictimInfo.VictimAge", 
    "VictimInfo.VictimGender", 
    "VictimInfo.InjuryType"
).agg(
    count("CrimeType").alias("TotalCrimes"),
    avg("OtherFactors.PoliceResponseTime").alias("AvgPoliceResponseTime")
)  


# Display behavior analysis
victim_behavior = victim_analysis.writeStream\
    .outputMode("complete")\
    .format("console")\
    .start()
    
victim_behavior.awaitTermination()


# Police Response Time Analysis
Police_response_time_analysis = parsed_df.groupBy("OtherFactors.WeatherConditions").agg(
    count("CrimeType").alias("TotalCrimes"),
    avg("OtherFactors.PoliceResponseTime").alias("AvgPoliceResponseTime")
)    



# Display behavior analysis
Police_response_behavior = Police_response_time_analysis.writeStream\
    .outputMode("complete")\
    .format("console")\
    .start()
    
Police_response_behavior.awaitTermination()



 