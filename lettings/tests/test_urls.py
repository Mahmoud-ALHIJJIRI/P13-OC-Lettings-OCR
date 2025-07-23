from django.urls import reverse, resolve
from lettings.views import lettings_index, get_letting


def test_lettings_index_url_resolves():
    """
    🧭 Test that the 'lettings:index' URL name resolves to the correct view function.
    """
    # 🔁 Reverse the URL from its name
    url = reverse('lettings:index')

    # 🔍 Resolve the URL to a view function
    resolved_view = resolve(url).func

    # ✅ Assert the correct function is matched
    assert resolved_view == lettings_index


def test_letting_detail_url_resolves():
    """
    🧭 Test that the letting detail URL resolves to the correct view function.
    """
    # 🔁 Reverse the URL with a sample letting ID
    url = reverse('lettings:letting', args=[42])

    # 🔍 Resolve the URL to a view function
    resolved_view = resolve(url).func

    # ✅ Assert the correct function is matched
    assert resolved_view == get_letting
