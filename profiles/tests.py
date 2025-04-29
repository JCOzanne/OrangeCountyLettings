import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from profiles.models import Profile

client = Client()

# testing Models


@pytest.mark.django_db
def test_profile_str():
    """
    Test the string representation of a Profile object.
    Create a Profile object and verify that its string representation
    matches the expected format.
    :return: None
    """
    user = User.objects.create(username="john")
    profile = Profile.objects.create(user=user, favorite_city="Lyon")
    assert str(profile) == "john"

# testing views and urls


@pytest.mark.django_db
def test_profiles_index_view():
    """
    Test the profiles index view.
    Verify that the profiles index view returns a 200 status code
    and that the response content contains the expected HTML.
    :return: None
    """
    response = client.get(reverse('profiles:index'))
    assert response.status_code == 200
    assert b'<h1>Profiles</h1>' in response.content


@pytest.mark.django_db
def test_profile_detail_view():
    """
    Test the profile detail view.
    Verify that the profile detail view returns a 200 status code
    and that the response content contains the expected HTML.
    :return: None
    """
    user = User.objects.create(username="lucie")
    Profile.objects.create(user=user, favorite_city="Paris")
    url = reverse('profiles:profile', args=["lucie"])
    response = client.get(url)
    assert response.status_code == 200
    assert b'Paris' in response.content
