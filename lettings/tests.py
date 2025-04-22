import pytest
from lettings.models import Letting, Address
from django.urls import reverse
from django.test import Client

#testing models#

@pytest.mark.django_db
def test_address_str():
    """
    Test the string representation of an Address object.
    Create an Address object and verify that its string representation
    matches the expected format.
    :return: None
    """
    address = Address.objects.create(
        number=123,
        street="Main Street",
        city="Cityville",
        state="CA",
        zip_code=12345,
        country_iso_code="USA"
    )
    assert str(address) == "123 Main Street"

@pytest.mark.django_db
def test_letting_str():
    """
    Test the string representation of a Letting object.
    Create a Letting object and verify that its string representation
    matches the expected format.
    :return: None
    """
    address = Address.objects.create(
        number=123, street="Main", city="City", state="ST", zip_code=12345, country_iso_code="FR"
    )
    letting = Letting.objects.create(title="Sunny Apartment", address=address)
    assert str(letting) == "Sunny Apartment"

#testing views and urls#

client = Client()

@pytest.mark.django_db
def test_lettings_index_view():
    """
    Test the lettings index view.
    Verify that the lettings index view returns a 200 status code
    and that the response content contains the expected HTML.
    :return: None
    """
    url = reverse('lettings:index')
    response = client.get(url)
    assert response.status_code == 200
    assert b'<h1>Lettings</h1>' in response.content

@pytest.mark.django_db
def test_letting_detail_view():
    """
    Test the letting detail view.
    Verify that the letting detail view returns a 200 status code
    and that the response content contains the expected HTML.
    :return: None
    """

    address = Address.objects.create(number=1, street="Rue Pasteur", city="Paris", state="FR", zip_code=75015, country_iso_code="FR")
    letting = Letting.objects.create(title="Appartement Parisien", address=address)

    url = reverse('lettings:letting', args=[letting.id])
    response = client.get(url)
    assert response.status_code == 200
    assert b'Appartement Parisien' in response.content

