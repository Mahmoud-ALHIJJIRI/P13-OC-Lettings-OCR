import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_index_view(client):
    """
    ✅ Test: Profiles Index View
    ➤ Ensures that the index page for profiles:
      - Returns HTTP 200 OK
      - Contains the word 'Profiles' in the response
    """
    # 🔗 Generate the URL for the profiles index view
    url = reverse('profiles:index')

    # 🌐 Send a GET request to the index page
    response = client.get(url)

    # ✅ Assert the response status is 200 OK
    assert response.status_code == 200

    # 🔍 Check that the response contains expected content
    assert b"Profiles" in response.content


@pytest.mark.django_db
def test_profile_detail_view(client):
    """
    ✅ Test: Profile Detail View
    ➤ Ensures that a user's profile page:
      - Returns HTTP 200 OK
      - Displays the user's favorite city
    """
    # 👤 Create a test user
    user = User.objects.create(username='jane_doe')

    # 🏙️ Create a profile for the user
    Profile.objects.create(user=user, favorite_city='London')

    # 🔗 Generate the URL for the profile detail view
    url = reverse('profiles:profile', args=['jane_doe'])

    # 🌐 Send a GET request to the profile detail page
    response = client.get(url)

    # ✅ Assert the response status is 200 OK
    assert response.status_code == 200

    # 🔍 Check that the favorite city is shown in the response
    assert b"London" in response.content
