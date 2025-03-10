import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

SERVICE_NAME = "GENERIC_SERVICE"

POSTGRES_HOST = os.getenv("", "localhost")
POSTGRES_PORT = os.getenv("", 5432)
POSTGRES_USER = os.getenv("", "keven")
POSTGRES_PASSWORD = os.getenv("", "kevenpassword")
POSTGRES_DB = os.getenv("", "keven_db")


class Config(BaseModel):
    POSTGRES_HOST: str = Field(default=POSTGRES_HOST)
    POSTGRES_PORT: int = Field(default=POSTGRES_PORT, ge=1024, le=65535)
    POSTGRES_USER: str = Field(default=POSTGRES_USER)
    POSTGRES_PASSWORD: str = Field(default=POSTGRES_PASSWORD)
    POSTGRES_DB: str = Field(default=POSTGRES_DB)
    DATABASE_ECHO: bool = Field(default=False)
    CONNECT_TIMEOUT: int = Field(default=20)

    @property
    def postgres_host(self):
        return self.POSTGRES_HOST

    @property
    def postgres_port(self):
        return str(self.POSTGRES_PORT)

    @property
    def postgres_user(self):
        return self.POSTGRES_USER

    @property
    def postgres_password(self):
        return self.POSTGRES_PASSWORD

    @property
    def postgres_db(self):
        return self.POSTGRES_DB

    @property
    def postgres_uri(self):
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"

    @property
    def database_echo(self):
        return self.DATABASE_ECHO

    @property
    def connect_timeout(self):
        return self.CONNECT_TIMEOUT

config = Config()