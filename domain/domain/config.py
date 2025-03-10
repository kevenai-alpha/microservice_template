from keven_core.configuration import BaseConfig

class Config(BaseConfig):
    LOCAL_CONFIG_FIELD: str = "local_config"

config = Config()