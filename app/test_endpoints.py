# app/test_endpoints.py

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers['content-type']
    assert "<h1>Code On!</h1>" in response.text  # ✅ Now matches your HTML
    assert "123" in response.text  # Still checks that abc="123" was rendered
def test_post_home():
    response = client.post("/")
    assert response.status_code == 200
    assert "application/json" in response.headers['content-type']
    assert response.json() == {"message": "You posted to the homepage. Thanks!"}