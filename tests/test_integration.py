import requests
import time


def test_health_endpoint():
    # чекаємо, поки Flask підніметься
    time.sleep(2)
    response = requests.get("http://localhost:5000/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"