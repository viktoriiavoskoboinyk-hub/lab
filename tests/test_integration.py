import requests
import time
import os


def test_service_add():
    # припускаємо, що сервіс піднятий на localhost:5000
    resp = requests.get("http://localhost:5000/add/2/3", timeout=5)
    assert resp.status_code == 200
    assert resp.json()["result"] == 5
