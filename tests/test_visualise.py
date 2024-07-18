# tests/test_visualize.py

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
    # Upload a test file for visualization tests
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


def test_visualize_histogram():
    file_id = "test_file_id"
    columns = ["col1"]
    response = client.get(f"/api/visualize/{file_id}?chart_type=histogram&columns={','.join(columns)}")
    assert response.status_code == 404  # File not found, expected for this test setup


def test_visualize_histogram_valid_file():
    response = client.post("/api/upload", files={"file": ("test.csv", b"col1,col2\n1,2\n3,4\n", "text/csv")})
    assert response.status_code == 200
    file_id = response.json()["file_id"]
    columns = ["col1"]
    response = client.get(f"/api/visualize/{file_id}?chart_type=histogram&columns={','.join(columns)}")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"


def test_visualize_scatter_plot():
    file_id = "test_file_id"
    columns = ["col1", "col2"]
    response = client.get(f"/api/visualize/{file_id}?chart_type=scatter&columns={','.join(columns)}")
    assert response.status_code == 404  # File not found, expected for this test setup


def test_visualize_scatter_plot_valid_file():
    response = client.post("/api/upload", files={"file": ("test.csv", b"col1,col2\n1,2\n3,4\n", "text/csv")})
    assert response.status_code == 200
    file_id = response.json()["file_id"]
    columns = ["col1", "col2"]
    response = client.get(f"/api/visualize/{file_id}?chart_type=scatter&columns={','.join(columns)}")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
