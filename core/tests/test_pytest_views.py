import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse


@pytest.mark.parametrize('param', [
    ('users:register-user'),
    ('users:login-user'),
    ('users:logout-user'),

])
def test_user_urls_views_response(client, param):
    """Test reponse of users views"""

    temp_url = reverse(param)
    response = client.get(temp_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_creation_view(client, user_data):
    """Test if user is created in db."""
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    register_url = reverse('users:register-user')
    response = client.post(register_url, data=user_data)

    assert get_user_model().objects.all().count() == 1
