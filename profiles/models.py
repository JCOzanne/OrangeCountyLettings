"""
This module defines the model for the profile's app.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user's profile.
    Extends the Django User model with additional information, such as favorite city.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        """
        Metadata for the Profile model.
        Specifies the database table name.
        """
        db_table = 'oc_lettings_site_profile'
