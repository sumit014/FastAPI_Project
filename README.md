FastAPI Data Analysis and Visualization API
This project implements a RESTful API using FastAPI in Python, focusing on data analysis and visualization functionalities. The API allows users to upload CSV files, perform data analysis (summary statistics), apply data transformations (such as normalization and handling missing values), and generate visualizations (e.g., histograms, scatter plots).

# Installation

## Clone the repository
1. `git clone https://github.com/sumit014/fastapi_project.git`
2. `cd fastapi_project`
3. Install dependencies using following command: `pip install -r requirements.txt`
### The installation is completed.

# Paths

`api/`: Contains endpoint definitions (endpoints/) and utility functions (`utils/`).

`tests/`: Includes test scripts for endpoint functionalities.

`uploads/`: Directory for storing uploaded CSV files.

`main.py`: Entry point of the FastAPI application.

`requirements.txt`: Lists dependencies required to run the application.

# Endpoints

The API exposes the following endpoints:

### Data Upload Endpoint:

Endpoint: /upload

Method: POST

Description: Accepts a CSV file and stores it for further processing.

**Note:** Please go to the path `http://127.0.0.1:8000/static/upload.html` to upload the file. It is a simple UI to choose and upload the file.

### Data Summary Endpoint:

Endpoint: /summary/<file_id>

Method: GET

Description: Provides a summary of the uploaded data including descriptive statistics and data types of each column.

### Data Transformation Endpoint:

Endpoint: /transform/<file_id>

Method: POST

Description: Applies transformations to the data (e.g., normalization, handling missing values).

### Data Visualization Endpoint:

Endpoint: /visualize/<file_id>

Method: GET

Description: Generates visualizations (e.g., histograms, scatter plots) based on specified columns.

# Running the API
To start the FastAPI application, run the following command:

`uvicorn main:app --reload`

This will start the development server, and you can access the API documentation (Swagger UI) at http://127.0.0.1:8000/docs and the alternative interactive documentation (ReDoc) at http://127.0.0.1:8000/redoc.

# Testing
Unit tests are implemented using **Pytest** framework. To run the tests, execute the following command:
`pytest`

**Note:** Before running the pytest command, make sure `requests` library is installed.

Ensure that all tests pass successfully before making changes or deploying the application.

# Dependencies
The project requires the following Python packages:

fastapi: Web framework for building APIs.
uvicorn: ASGI server for running FastAPI applications.
matplotlib: Library for data visualization.
pandas: Library for data manipulation and analysis.
pytest: Testing framework for Python.
pydantic: Data validation and settings management library.
requests: Library to make sure pytest executes without error.

These dependencies are listed in requirements.txt and can be installed via pip.

# Test Collection for API Testing

Providing collections of the API endpoints in the directory to run and test the endpoints using Insomnia.(We can use Postman too)