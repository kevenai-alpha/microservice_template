
import signal
from api.api_main import app
from services.grpc.grpc_main import get_grpc_server
from services.kafka.kafka_main import get_producer, consume_messages
from svc_logger import logger
from config import config


# Configuration

def serve_grpc():
    server = get_grpc_server()
    server.add_insecure_port(f'[::]:{config.grpc_port}')
    server.start()
    logger.info(f"gRPC server started on port {config.grpc_port}")
    server.wait_for_termination()

def serve_internal_grpc():
    internal_server = get_grpc_server()
    internal_server.add_insecure_port(f'[::]:{config.internal_grpc_port}')
    internal_server.start()
    logger.info(f"Internal gRPC server started on port {config.internal_grpc_port}")
    internal_server.wait_for_termination()

def shutdown_handler(signal_received, frame):
    logger.info("Shutting down services")
    producer.close()
    exit(0)
# Start Services
if __name__ == "__main__":
    producer = get_producer(config.kafka_topic)
    serve_grpc()
    serve_internal_grpc()
    app.run(host="0.0.0.0", port=int(config.http_port))
    # Start Kafka Consumer
    consume_messages(config.kafka_topic, config.kafka_broker, logger)

    # Register shutdown handler
    signal.signal(signal.SIGINT, shutdown_handler)
    signal.signal(signal.SIGTERM, shutdown_handler)