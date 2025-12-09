from fastapi.testclient import TestClient
from app.main import app
import re
import pytest
import httpx

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "status" in response.json()
    assert isinstance(response.json()["status"], str)
    assert len(response.json()["status"]) > 0
    msg = response.json()["status"].lower()
    assert re.search(r"running|ready|healthy", msg)


def test_root_endpoint_server():
    try:
        response = httpx.get("http://localhost:8000/")
    except Exception:
        pytest.fail("❌ Server is not running or refused the connection")

    assert response.status_code == 200
    data = response.json()

    assert "status" in data
    assert isinstance(data["status"], str)
    assert len(data["status"]) > 0

def test_prediction():
    response = client.post("/predict", params={"text": "This is good"})
    assert response.status_code == 200
    assert response.json()["label"] == "positive"