import json
import logging
SERVICE_NAME = "generic_microservice"
LOG_LEVEL = logging.INFO

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_message = {
            "level": record.levelname,
            "service": SERVICE_NAME,
            "message": record.getMessage(),
            "timestamp": self.formatTime(record, self.datefmt),
        }
        return json.dumps(log_message)

logger = logging.getLogger(SERVICE_NAME)
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)
