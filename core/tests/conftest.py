import pytest


@pytest.fixture
def user_data():
    return {
        'username': 'email',
        'password': 'testpass123',
        'full_name': 'Stefan'
    }
