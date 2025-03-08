import os
import time

from kafka import KafkaProducer, KafkaConsumer



KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "keven_events")

# Kafka Setup
def get_producer(cfg):
    return KafkaProducer(bootstrap_servers=cfg.kafka_broker)

def consume_messages(cfg, svc_logger):
    try:
        consumer = KafkaConsumer(cfg.kafka_topic, bootstrap_servers=cfg.kafka_broker, auto_offset_reset='earliest')
        for message in consumer:
            svc_logger.info("Received Kafka message: %s", message.value.decode("utf-8"))
    except Exception as e:
        svc_logger.error(f"Kafka connection failed: {e}. Retrying in 5s...")
        time.sleep(5)
