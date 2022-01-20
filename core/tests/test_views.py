from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


CREATE_TICKET_URL = reverse('tickets:create-ticket')


class TestTicketCreateView(TestCase):
    """Test case for TicketCreateView."""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            password='test1231',
        )
        self.client = Client()

    def test_create_ticket_view_with_no_user(self):
        """Test TicketCreateView while user is not logged in."""
        data = {
            'title': 'test title',
            'description': 'test',
            'importance': 'low',
        }
        response = self.client.post(CREATE_TICKET_URL, data=data)
        self.assertEquals(response.status_code, 302)


    def test_create_ticket_view_user_loggedin(self):
        """Test TicketCreateView with authenticated user."""
        data = {
            'title': 'test title',
            'description': 'test',
            'importance': 'low',
            'created_by': self.user,
        }
        self.client.force_login(self.user)
        response = self.client.post(CREATE_TICKET_URL, data=data)
        self.assertEquals(response.status_code, 200)