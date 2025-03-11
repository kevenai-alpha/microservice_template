# Services Submodule

## Overview
The `services` submodule is responsible for handling the core functionalities of a KEVEN microservice. It provides the following key features:

- **gRPC Server**: Implements gRPC endpoints for inter-service communication.
- **Internal gRPC Server**: Runs a separate internal gRPC server for secured microservice interactions.
- **REST API**: Provides an optional Flask-based RESTful API for external interactions.
- **Kafka Integration**: Supports Kafka-based event-driven communication by publishing and consuming messages.
- **Threaded Execution**: Uses `concurrent.futures.ThreadPoolExecutor` to run gRPC, Kafka, and REST services concurrently.

---

## Installation & Usage

### **1. Installing Poetry**
Ensure that Poetry is installed before managing dependencies:
```sh
curl -sSL https://install.python-poetry.org | python3 -

After installation, verify the installation by running:
```sh
poetry --version
```

### **2. Installing Dependencies**
Navigate to the `services` directory and install the required dependencies:
```sh
cd services
poetry install
``` 
This will install the required dependencies in a virtual environment.

### **3. Running the Service**
To run the service, execute the following command:
```sh
poetry run python -m services
```
This will start the gRPC server, internal gRPC server, REST API, and Kafka integration.

### **4. Adding New Dependencies**
To add new dependencies, use the following command:
```sh
poetry add <package-name>
```
This will add the specified package to the `pyproject.toml` file and install it in the virtual environment.

### **5. Running Tests**
To run the tests, execute the following command:
```sh
poetry run pytest
```
This will run the test cases defined in the `tests` directory.


### **6. Linting**
To run the linters, execute the following commands:
```sh
poetry run black services -l 79
poetry run flake8 services --ignore=E203,W503,W504
```
---

