"""
This module contains unit tests to verify the behavior of the Django application in various scenarios. The tests include:

- A dummy test to verify that the test environment is functioning correctly.
- A test to verify that accessing a nonexistent page returns a 404 error.
- A test to verify that accessing a page that generates an internal error returns a 500 error.

The tests use pytest and the Django test client to simulate HTTP requests and verify responses.

Test functions:
- test_dummy(): Dummy test to verify the test environment.
- test_404_page(): Test to verify the 404 error page.
- test_500_page(): Test to verify the 500 error page.
"""

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
