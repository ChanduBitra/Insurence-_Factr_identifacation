from fastapi.testclient import TestClient
import main
from fastapi import status


client = TestClient(main.app)

def test_return_health_check():
    response = client.get('health')
    assert response.status_code == status.HTTP_200_OK
