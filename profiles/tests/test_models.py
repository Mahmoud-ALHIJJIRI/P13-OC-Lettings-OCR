import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_str():
    """
    ✅ Test: Profile __str__ Method
    ➤ Ensures that the string representation of a Profile returns the username.
    """
    # 👤 Create a test user
    user = User.objects.create(username='john_doe')

    # 🏙️ Create a profile linked to the test user
    profile = Profile.objects.create(user=user, favorite_city='Paris')

    # 🔍 Check that str(profile) returns the username
    assert str(profile) == 'john_doe'
