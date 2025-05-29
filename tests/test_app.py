def test_home():
    from app.main import app as app1
    client = app1.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"CI/CD in Python is working!" in response.data
    response1 = client.get("/abc")
    assert response1.status_code == 200
    assert b"A is for apple, B is for ball, C is for Cat" in response1.data