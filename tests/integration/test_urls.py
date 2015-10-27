import pytest

pytestmark = pytest.mark.django_db


def test_urls(client):
    response = client.get('/abc')
    assert response.status_code == 404

    response = client.get('/auth/register/')
    assert response.status_code == 405

    response = client.get('/auth/activate/')
    assert response.status_code == 405 # Method Not Allowed


  
