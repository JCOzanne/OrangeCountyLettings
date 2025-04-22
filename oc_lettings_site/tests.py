from django.test import Client

client = Client()

def test_dummy():
    assert 1

def test_404_page():
    """
    Test 404 error page.
    Verify that accessing a non-existent page returns a 404 status code
    and that the response content contains the expected error message.
    :return: None
    """
    response = client.get('/thispagedoesnotexist/')
    assert response.status_code == 404
    assert b"La page que vous recherchez n'existe pas" in response.content