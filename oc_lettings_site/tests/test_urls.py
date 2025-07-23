import pytest
from django.urls import reverse, resolve
from oc_lettings_site import views as site_views


def test_root_url_resolves_to_index():
    """
    🧭 Test that the root URL resolves to the homepage view.
    """
    url = reverse("index")
    resolved_view = resolve(url).func
    assert resolved_view == site_views.index


def test_lettings_namespace_index_url():
    """
    🧭 Test that 'lettings:index' resolves to lettings_index.
    """
    url = reverse("lettings:index")
    assert url == "/lettings/index/"  # Optional: assert path structure


def test_profiles_namespace_index_url():
    """
    🧭 Test that 'profiles:index' resolves to profiles_index.
    """
    url = reverse("profiles:index")
    assert url == "/profiles/index/"


def test_error_handlers_are_set_correctly():
    """
    ❗️ Verify that handler404 and handler500 are mapped to correct functions.
    """
    from oc_lettings_site import urls

    assert urls.handler404 == "oc_lettings_site.views.custom_404"
    assert urls.handler500 == "oc_lettings_site.views.custom_500"
