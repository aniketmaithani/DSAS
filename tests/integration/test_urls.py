from django.test import Client


def test_urls_abc():
	client = Client()
    response = client.get('/abc/')
    assert response.status_code == 404

    response = client.get('/auth/register/')
    assert response.status_code == 405

    response = client.get('/auth/activate/')
    assert response.status_code == 401 # UnAuthorized Access


  
