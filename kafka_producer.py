import json

from kafka import KafkaProducer

if __name__ == '__main__':
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    for i in range(3):
        message = producer.send('test', {
            "message": f"hello from producer ({i})"
        })
        result = message.get(timeout=60)
        print(result)
