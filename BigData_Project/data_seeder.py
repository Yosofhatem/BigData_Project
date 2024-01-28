import time
from Kafka import Kafka
from data_faker import DataFaker



# Produce a few sample messages to the Kafka topic
for _ in range(400):
    sample_data = DataFaker.generate_random_data()
    Kafka.produce_message('Crimetopic', sample_data)
    time.sleep(1)  # Add a delay to simulate real-time data