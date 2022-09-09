from kafka import KafkaConsumer, KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic


import argparse
from time import sleep



#Default config
kafka_server = 'localhost:9092'

#Default values
topic   = 'Default-topic'
message = 'Hello.'
n_messages = 10



def list_topics():
	cons = KafkaConsumer(bootstrap_servers=kafka_server)
	return cons.topics()

def create_topic(topic):
	global admin_client
	if not admin_client:
		admin_client = KafkaAdminClient(bootstrap_servers=kafka_server)

	if topic not in list_topics():
		topic_list = []
		topic_list.append(NewTopic(name=topic, num_partitions=1, replication_factor=1))
		admin_client.create_topics(new_topics=topic_list, validate_only=False)
	else:
		return False
	return True
	
def producer(topic, message, n=10):
	prod = KafkaProducer(bootstrap_servers=kafka_server)

	for i in range(n):
		print(f'- {message} - {i} -')
		prod.send(topic, f' {message} {i}'.encode())
	prod.flush()

def consumer(topic):
	cons = KafkaConsumer(topic, bootstrap_servers=kafka_server)

	for message in cons:
		print(message.value.decode())

	
if __name__ == '__main__':
	
	parser = argparse.ArgumentParser()
	parser.add_argument('--type',
		help='Operation type',
		type=str,
		choices=['producer', 'consumer', 'register', 'list'], 
		required=True)
	parser.add_argument('-t', '--topic',
		help='Topic to be used',
		type=str)
	parser.add_argument('-m', '--message',
		help='Message to be produced',
		type=str)
	parser.add_argument('-n', '--num_messages',
		help='Number of messages to be produced',
		type=int)

	args = parser.parse_args()

	#Topic
	if args.topic:
		topic = args.topic
	#Message
	if args.message:
		message = args.message
	if args.num_messages:
		n_messages = args.num_messages


	#Type
	if args.type:
		#Producer
		if args.type == 'producer':
			producer(topic, message, n_messages)
		#Consumer
		if args.type == 'consumer':
			if topic in list_topics():
				consumer(topic)
			else:
				print(f'{topic} is not registered as a topic.')
		#Create a topic
		if args.type == 'register':
			if not create_topic(topic):
				print(f'{topic} is already registered as a topic.')
		#List topics
		if args.type == 'list':
			print(f'Topics: {list_topics()}')
		


