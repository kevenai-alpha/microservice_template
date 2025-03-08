import logging
SERVICE_NAME = "generic_microservice"
LOG_LEVEL = logging.INFO

# Logging Setup
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(SERVICE_NAME)