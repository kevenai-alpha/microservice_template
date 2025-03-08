import os

from dotenv import load_dotenv
from kafka import KafkaProducer, KafkaConsumer
from pydantic import BaseModel

from api.api_main import app
from services.grpc.grpc_main import get_grpc_server
from services.kafka.kafka_main import get_producer, consume_messages
from svc_logger import logger

# Load environment variables
load_dotenv()

# Configuration

GRPC_PORT = os.getenv("GRPC_PORT", "50051")
INTERNAL_GRPC_PORT = os.getenv("INTERNAL_GRPC_PORT", "50052")
HTTP_PORT = os.getenv("HTTP_PORT", "5000")
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "keven_events")

def serve_grpc():
    server = get_grpc_server()
    server.add_insecure_port(f'[::]:{GRPC_PORT}')
    server.start()
    logger.info(f"gRPC server started on port {GRPC_PORT}")
    server.wait_for_termination()

def serve_internal_grpc():
    internal_server = get_grpc_server()
    internal_server.add_insecure_port(f'[::]:{INTERNAL_GRPC_PORT}')
    internal_server.start()
    logger.info(f"Internal gRPC server started on port {INTERNAL_GRPC_PORT}")
    internal_server.wait_for_termination()


# Start Services
if __name__ == "__main__":
    producer = get_producer(KAFKA_TOPIC)
    serve_grpc()
    serve_internal_grpc()
    app.run(host="0.0.0.0", port=int(HTTP_PORT))
    # Start Kafka Consumer
    consume_messages(KAFKA_TOPIC, KAFKA_BROKER, logger)
