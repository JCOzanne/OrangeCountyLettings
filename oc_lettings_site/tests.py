import pytest
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


@pytest.mark.django_db
def test_500_page(settings):
    """
    Tests the 500 Internal Server Error page for proper handling and messaging. The test ensures
    that when the DEBUG setting is disabled, an HTTP 500 response is returned for a view that
    raises an unhandled exception. The test also verifies that the appropriate error message is
    displayed on the resulting page.

    :param settings: Django settings object used for configuring the application
    :return: None
    """
    settings.DEBUG = False

    test_client = Client(raise_request_exception=False)
    response = test_client.get("/sentry-key-error/")

    assert response.status_code == 500
    assert ("Une erreur interne est survenue. Veuillez réessayer plus tard."
            in response.content.decode())
