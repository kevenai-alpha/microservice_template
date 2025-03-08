
from flask import Flask, jsonify, request
# Flask App for REST API
app = Flask(__name__)

# REST API Route Example
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "OK", "service": SERVICE_NAME})

@app.route("/publish", methods=["POST"])
def publish_event():
    data = request.json
    producer.send(KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
    return jsonify({"status": "Message Published"})