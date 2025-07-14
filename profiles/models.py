"""
👤 Models for the profiles app.
Defines user-related data such as favorite city.
"""
from django.db import models
from django.contrib.auth.models import User


# 👤 Profile model
class Profile(models.Model):
    """Extends the built-in User model with a favorite city."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='custom_profile'
    )
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Return the username as the string representation."""
        return self.user.username
