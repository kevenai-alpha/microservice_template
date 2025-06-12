import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from domain.config import Config

# Load environment variables
#load_dotenv()

SERVICE_NAME = "GENERIC_SERVICE"


class Config(Config):
    LOCAL_DB_FIELD: str = "local_db"
    CONNECT_TIMEOUT: int = 10
    @property
    def postgres_uri(self):
        if user := getattr(self, 'postgres_user', None):
            if pwd := getattr(self, 'postgres_password', None):
                if host := getattr(self, 'postgres_host', None):
                    if port := getattr(self, 'postgres_port', None):
                        if db := getattr(self, 'postgres_db', None):
                            return f"postgresql://{user}:{pwd}@{host}:{port}/{db}"
        raise Exception("Missing postgres configuration.  Check: postgres_user, postgres_password, "
                        "postgres_host, postgres_port, postgres_db")


config = Config()