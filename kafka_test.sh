
#Create topic
kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic 'hello'

#List topics
kafka-topics.sh --list --bootstrap-server kafka:9092

#Producer
kafka-console-producer.sh --request-required-acks 1 --broker-list kafka:9092 --topic 'hello'

#Consumer
kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic 'hello'


