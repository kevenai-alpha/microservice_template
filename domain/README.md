# Services Submodule

## Overview
The `domain` submodule is responsible for  defining core business logic, domain models, and data validation structures. It serves as a pure business logic layer, ensuring that core functionalities are decoupled from database persistence and service operations.

### Features
- **Encapsulation of Business Logic**: Ensures that logic is centralized and reusable.
- **Data Validation**: Uses Pydantic to validate models before processing.
- **Independence from Services and Database**: Does not rely on external service integrations or database access.
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
Navigate to the `domain` directory and install the required dependencies:
```sh
cd services
poetry install
``` 
This will install the required dependencies in a virtual environment.
### **3. Installing the Domain subpackage**
To install the domain submodule as a package from the local repository:
```sh
poetry add generic_microservice_domain --source keven-local
```
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

