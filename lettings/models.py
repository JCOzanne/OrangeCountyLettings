"""
This module defines the models for the lettings app.

It includes two models:
- Address: Represents a physical address.
- Letting: Represents a property letting, linking a title to a specific address.
"""


from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """
    Represents a physical address.
    Stores address details including number, street, city, state, zip code, and country ISO code.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'

    class Meta:
        """
        Metadata for the Address model.

        Specifies the database table name.
        """
        db_table = "oc_lettings_site_address"
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Represents a property letting.
    Links a title to a specific address.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        """
        Metadata for the Letting model.
        Specifies the database table name.
        """
        db_table = "oc_lettings_site_letting"
