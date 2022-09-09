from kafka import KafkaConsumer


consumer = KafkaConsumer('hello', bootstrap_servers='localhost:9092')

for message in consumer:
  print(message.value.decode())
