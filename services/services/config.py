import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

SERVICE_NAME = "GENERIC_SERVICE"

GRPC_PORT = os.getenv("GRPC_PORT", "50051")
INTERNAL_GRPC_PORT = os.getenv("INTERNAL_GRPC_PORT", "50052")
HTTP_PORT = os.getenv("HTTP_PORT", "5000")
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "keven_events")


class Config(BaseModel):
    GRPC_PORT: int = Field(default=GRPC_PORT, ge=1024, le=65535)
    INTERNAL_GRPC_PORT: int = Field(default=INTERNAL_GRPC_PORT, ge=1024, le=65535)
    HTTP_PORT: int = Field(default=HTTP_PORT, ge=1024, le=65535)
    KAFKA_BROKER: str = Field(default=KAFKA_BROKER, regex=r"^[a-zA-Z0-9._-]+:\d+$")
    KAFKA_TOPIC: str = Field(default=KAFKA_TOPIC)
    SERVICE_NAME: str = Field(default=SERVICE_NAME)

    @property
    def service_name(self):
        return self.SERVICE_NAME

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