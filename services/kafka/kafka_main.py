import os
from kafka import KafkaProducer, KafkaConsumer

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "keven_events")

# Kafka Setup
def get_producer(kfka_broker):
    return KafkaProducer(bootstrap_servers=kfka_broker)

def consume_messages(kfka_topic, kfka_broker, svc_logger):
    consumer = KafkaConsumer(kfka_topic, bootstrap_servers=kfka_broker, auto_offset_reset='earliest')
    for message in consumer:
        svc_logger.info("Received Kafka message: %s", message.value.decode("utf-8"))
