import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.security import create_access_token

client = TestClient(app)

def test_create_and_verify_token():
    token = create_access_token({"sub": "testuser"})
    response = client.post("/process-events", headers={"Authorization": f"Bearer {token}"}, json={"from_block": 1, "to_block": 100})
    assert response.status_code == 200

def test_invalid_token():
    response = client.post("/process-events", headers={"Authorization": "Bearer invalid_token"}, json={"from_block": 1, "to_block": 100})
    assert response.status_code == 401