# kafka_producer-consumer
Producer and consumer using Python and Apache Kafka.

To initialize Kafka:  
`docker-compose up`

To register a topic:
`python prodcons.py --type register -t TOPIC`

To list all registered topics:
`python prodcons.py --type list`

To consumer from a specific topic:
`python prodcons.py --type consumer -t TOPIC`
(Ctrl +c to stop)

To produce messages on a specific topic:
`python prodcons.py --type producer -t TOPIC -m MESSAGE -n NUM_MESSAGES`

To shutdown Kafka:
`docker-compose down`