# tests/test_transform.py

import os
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
UPLOAD_FOLDER = "./uploads_test"


@pytest.fixture(scope="module", autouse=True)
def setup():
    # Setup
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    # Upload a test file for transformation tests
    file_content = b"col1,col2\n1,2\n3,4\n"
    files = {"file": ("test.csv", file_content, "text/csv")}
    response = client.post("/api/upload", files=files)
    assert response.status_code == 200
    yield
    # Teardown
    for file_name in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)


def test_transform_data():
    file_id = "test_file_id"
    transformations = {"normalize": ["col1"]}
    response = client.post(f"/api/transform/{file_id}", json={"transformations": transformations})
    assert response.status_code == 404  # File not found, expected for this test setup


def test_transform_data_valid_file():
    response = client.post("/api/upload", files={"file": ("test.csv", b"col1,col2\n1,2\n3,4\n", "text/csv")})
    assert response.status_code == 200
    file_id = response.json()["file_id"]
    transformations = {"normalize": ["col1"]}
    response = client.post(f"/api/transform/{file_id}", json={"transformations": transformations})
    assert response.status_code == 200
    assert "file_id" in response.json()
    transformed_file_id = response.json()["file_id"]
    assert transformed_file_id != file_id
