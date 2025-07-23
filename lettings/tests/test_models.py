import pytest
from django.core.exceptions import ValidationError
from lettings.models import Address


def make_address(**overrides):
    """
    🏗️ Factory to create a valid Address object with optional overrides.
    Useful for validation edge cases.
    """
    defaults = {
        "number": 10,
        "street": "Generic Street",
        "city": "City",
        "state": "FR",
        "zip_code": 75000,
        "country_iso_code": "FRA"
    }
    defaults.update(overrides)
    return Address(**defaults)


@pytest.mark.django_db
def test_address_str(address):
    """
    🧪 Test Address.__str__() returns 'number street'.
    """
    # ✅ Assert string output and a sample field
    assert str(address) == "42 Rue de Test"
    assert address.zip_code == 75001


@pytest.mark.django_db
def test_letting_str(letting):
    """
    🧪 Test Letting.__str__() returns the title.
    """
    assert str(letting) == "Test Letting"


@pytest.mark.django_db
def test_address_max_zip_code_validation():
    """
    🚫 Test zip_code above 99999 raises ValidationError.
    """
    address = make_address(zip_code=100000)  # invalid
    with pytest.raises(ValidationError):
        address.full_clean()


@pytest.mark.django_db
def test_address_short_country_code():
    """
    🚫 Test country_iso_code shorter than 3 chars raises ValidationError.
    """
    address = make_address(country_iso_code="F")  # invalid
    with pytest.raises(ValidationError):
        address.full_clean()


@pytest.mark.django_db
def test_address_short_state_code():
    """
    🚫 Test state shorter than 2 chars raises ValidationError.
    """
    address = make_address(state="F")  # invalid
    with pytest.raises(ValidationError):
        address.full_clean()
