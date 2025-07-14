# 🗂️ Django Models for the Lettings App
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


# 🏡 Address Model
class Address(models.Model):
    """Represents a physical address."""

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(
        max_length=2,
        validators=[MinLengthValidator(2)]
    )
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)]
    )
    country_iso_code = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        """Return a readable address representation."""
        return f'{self.number} {self.street}'


# 🏘️ Letting Model
class Letting(models.Model):
    """Represents a rental listing (Letting)."""

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Return the title of the letting."""
        return self.title
