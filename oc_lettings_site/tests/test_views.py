import pytest
from unittest.mock import patch
from django.http import HttpResponse
from django.test import RequestFactory
from django.urls import reverse
from oc_lettings_site.views import custom_404, custom_500
from profiles.models import Profile
from django.contrib.auth.models import User, AnonymousUser


@pytest.mark.django_db
@patch("oc_lettings_site.views.render")
def test_index_view(mock_render, client):
    """
    🏠 Test index view without rendering the template (mocked).
    """
    # 🎭 Set up the mock return
    mock_render.return_value = HttpResponse("MOCK INDEX RENDER")

    user = User.objects.create(username="tester")
    Profile.objects.create(user=user, favorite_city="Paris")

    response = client.get(reverse("index"))

    assert response.status_code == 200
    mock_render.assert_called_once()
    assert "MOCK INDEX RENDER" in response.content.decode()


@patch("oc_lettings_site.views.render")
def test_custom_404_view(mock_render):
    """
    🚫 Test custom 404 view using a mocked render.
    """
    mock_render.return_value = HttpResponse("MOCK 404 RENDER", status=404)
    factory = RequestFactory()
    request = factory.get("/nonexistent/")
    response = custom_404(request, exception=None)

    assert response.status_code == 404
    mock_render.assert_called_once()
    assert "MOCK 404 RENDER" in response.content.decode()


@patch("oc_lettings_site.views.render")
def test_custom_500_view(mock_render):
    """
    💥 Test custom 500 view using a mocked render.
    """
    mock_render.return_value = HttpResponse("MOCK 500 RENDER", status=500)
    factory = RequestFactory()
    request = factory.get("/server-error/")
    request.user = AnonymousUser()
    response = custom_500(request)

    assert response.status_code == 500
    mock_render.assert_called_once()
    assert "MOCK 500 RENDER" in response.content.decode()
