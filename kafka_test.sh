#!/bin/bash

#Debug scripting. The recommendation is not to use it =/

TOPIC='hellowz'
MESSAGE='Hello world'

WAIT='3s'

docker-compose up -d

echo "Waiting $WAIT until cluster up"
sleep $WAIT

#Create topic
echo "Creating topic $TOPIC :"
docker-compose exec kafka kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic $TOPIC

#List topics
echo 'Listing topics:'
docker-compose exec kafka kafka-topics.sh --list --bootstrap-server kafka:9092

#Consumer
echo 'Opening consumer:'
docker-compose exec kafka -it kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic 'hello' &

sleep $WAIT

#Producer
echo "Producing message "
docker-compose exec kafka -it  kafka-console-producer.sh --request-required-acks 1 --broker-list kafka:9092 --topic $TOPIC <<< $MESSAGE



docker-compose down


