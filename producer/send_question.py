from kafka import KafkaProducer
import json

from config.kafka_config import KAFKA_BOOTSTRAP_SERVERS,KAFKA_TOPIC

producer=KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda m:json.dumps(m).encode('utf-8')
)

def ask_question(question):
    producer.send(KAFKA_TOPIC, {'question': question})
    producer.flush()