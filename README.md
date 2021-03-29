Test base images
________________
```
> docker-compose -f test/docker-compose.yml up -d zookeeper kafka_1 kafka_2

> test/runAllTests.sh
```
Compose "our" images
---------------------
```
docker-compose up -d
```
Test by python scripts
=======================
``` 
pip install kafka-python
```

In first terminal:
```
python kafka_consumer.py
```
In second terminal:
```
python kafka_producer.py
```

___________________________
Original repo: https://github.com/wurstmeister/kafka-docker
