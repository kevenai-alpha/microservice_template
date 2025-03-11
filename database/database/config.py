import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from domain.config import Config

# Load environment variables
#load_dotenv()

SERVICE_NAME = "GENERIC_SERVICE"


class Config(Config):
    LOCAL_DB_FIELD: str = "local_db"


config = Config()