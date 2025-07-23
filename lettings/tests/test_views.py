import pytest
from django.urls import reverse
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_lettings_index_view(client):
    """
    ✅ Test the lettings index view.
    Ensures it returns a 200 status and displays the letting title.
    """

    # 🏗️ Arrange: Create test address and letting
    address = Address.objects.create(
        number=42,
        street="Rue de Test",
        city="Paris",
        state="FR",
        zip_code=75001,
        country_iso_code="FRA"
    )
    Letting.objects.create(title="Test Letting", address=address)

    # 🚀 Act: Call the lettings index view
    url = reverse('lettings:index')
    response = client.get(url)

    # ✅ Assert: View returns status 200 and displays title
    assert response.status_code == 200
    assert b"Test Letting" in response.content


@pytest.mark.django_db
def test_get_letting_view(client):
    """
    ✅ Test the letting detail view.
    Ensures the correct letting and address content is shown.
    """

    # 🏗️ Arrange: Create an address and letting
    address = Address.objects.create(
        number=42,
        street="Rue de Test",
        city="Paris",
        state="FR",
        zip_code=75001,
        country_iso_code="FRA"
    )
    letting = Letting.objects.create(
        title="Letting Detail Test",
        address=address
    )

    # 🚀 Act: Request the letting detail page
    url = reverse("lettings:letting", args=[letting.pk])
    response = client.get(url)

    # ✅ Assert: Check response and presence of content
    assert response.status_code == 200
    content = response.content.decode()

    assert "Letting Detail Test" in content
    assert "Rue de Test" in content
    assert "Paris" in content
    assert "FR" in content
