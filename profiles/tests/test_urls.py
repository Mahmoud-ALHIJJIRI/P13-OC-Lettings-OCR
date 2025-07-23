from django.urls import reverse, resolve
from profiles.views import profiles_index, get_profile


def test_profiles_index_url():
    """
    ✅ Test: Profiles Index URL
    ➤ Ensures that the 'profiles:index' URL correctly resolves to the `profiles_index` view.
    """
    # 🔗 Reverse the named URL for the index view
    path = reverse('profiles:index')

    # 🔍 Resolve the URL and compare to the correct view function
    resolved_func = resolve(path).func
    assert resolved_func == profiles_index


def test_profile_detail_url():
    """
    ✅ Test: Profile Detail URL
    ➤ Ensures that the 'profiles:profile' URL with a username resolves to the `get_profile` view.
    """
    # 🔗 Reverse the URL for the profile detail view with a sample username
    path = reverse('profiles:profile', args=['some_username'])

    # 🔍 Resolve the URL and check if it maps to the correct view
    resolved_func = resolve(path).func
    assert resolved_func == get_profile
