def test_home():
    from app.main import app
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"CI/CD in Python is working!" in response.data
