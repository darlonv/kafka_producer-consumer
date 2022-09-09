from kafka import KafkaProducer

import time

topic   = 'Python'
message = 'Hello!'


producer = KafkaProducer(bootstrap_servers='localhost:9092')



print('Producer:')
for i in range(10):
	producer.send(topic, f' {message} {i}'.encode())
	
	producer.flush()
	time.sleep(1)
