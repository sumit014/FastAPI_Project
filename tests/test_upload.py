# tests/test_upload.py

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
    yield
    # Teardown
    for file_name in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)


def test_upload_file():
    file_content = b"col1,col2\n1,2\n3,4\n"
    files = {"file": ("test.csv", file_content, "text/csv")}
    response = client.post("/api/upload", files=files)
    assert response.status_code == 200
    assert "file_id" in response.json()
    file_id = response.json()["file_id"]
    file_path = os.path.join(UPLOAD_FOLDER, file_id + ".csv")
    assert os.path.exists(file_path)


def test_upload_file_missing_file():
    files = {"file": ("test.csv", b"", "text/csv")}
    response = client.post("/api/upload", files=files)
    assert response.status_code == 422


def test_upload_file_invalid_format():
    files = {"file": ("test.txt", b"Invalid file content", "text/plain")}
    response = client.post("/api/upload", files=files)
    assert response.status_code == 422
