import json

from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'test',
        bootstrap_servers="localhost:9092",
        value_deserializer=json.loads
    )
    for msg in consumer:
        print(msg)
