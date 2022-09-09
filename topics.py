#pip3 install kafka-python

from kafka import KafkaConsumer, KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic


kafka_server = 'localhost:9092'

admin_client = KafkaAdminClient(
    bootstrap_servers=kafka_server)

def create_topic(topic):
	if topic not in list_topics():
		topic_list = []
		topic_list.append(NewTopic(name=topic, num_partitions=1, replication_factor=1))
		admin_client.create_topics(new_topics=topic_list, validate_only=False)
	else:
		return False
	return True
	
def list_topics():
	consumer = KafkaConsumer(bootstrap_servers=kafka_server)
	return consumer.topics()
	
def producer(topic, message, n=10):
	for i in range(n):
		producer.send(topic, f' {message} {i}'.encode())


	
if __name__ == '__main__':
	create_topic('Testing')
	print(f'Topics: {list_topics()}')
	#producer('hello', 'python test', 20)
