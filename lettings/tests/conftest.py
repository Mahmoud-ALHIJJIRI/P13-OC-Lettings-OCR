import pytest
from lettings.models import Address, Letting


@pytest.fixture
def address():
    """
    🏡 Fixture: Create and return a sample Address instance.
    Used across multiple tests to avoid repetition.
    """
    return Address.objects.create(
        number=42,
        street="Rue de Test",
        city="Paris",
        state="FR",
        zip_code=75001,
        country_iso_code="FRA"
    )


@pytest.fixture
def letting(address):
    """
    🏘️ Fixture: Create and return a sample Letting instance.
    Depends on the address fixture.
    """
    return Letting.objects.create(
        title="Test Letting",
        address=address
    )
