def test_home():
    from app.main import app as app1
    client = app1.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"This is a CI/CD pipeline using flask!" in response.data
    response1 = client.get("/abc")
    assert response1.status_code == 200
    assert b"Fun with Alphabets" in response1.data