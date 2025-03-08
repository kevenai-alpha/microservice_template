from pydantic import BaseModel
import os
from dotenv import load_dotenv
# Load environment variables
load_dotenv()


GRPC_PORT = os.getenv("GRPC_PORT", "50051")
INTERNAL_GRPC_PORT = os.getenv("INTERNAL_GRPC_PORT", "50052")
HTTP_PORT = os.getenv("HTTP_PORT", "5000")
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "keven_events")


class Config(BaseModel):
    GRPC_PORT: str = GRPC_PORT
    INTERNAL_GRPC_PORT: str = INTERNAL_GRPC_PORT
    HTTP_PORT: str = HTTP_PORT
    KAFKA_BROKER: str = KAFKA_BROKER
    KAFKA_TOPIC: str = KAFKA_TOPIC

    @property
    def kafka_broker(self):
        return self.KAFKA_BROKER

    @property
    def kafka_topic(self):
        return self.KAFKA_TOPIC

    @property
    def grpc_port(self):
        return self.GRPC_PORT

    @property
    def internal_grpc_port(self):
        return self.INTERNAL_GRPC_PORT

    @property
    def http_port(self):
        return self.HTTP_PORT

config = Config