from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from tickets.models import Ticket


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

        response = self.client.post(CREATE_TICKET_URL)
        self.assertEquals(response.status_code, 302)


    def test_create_ticket_view_user_loggedin(self):
        """Test TicketCreateView with authenticated user."""

        self.client.force_login(self.user)
        response = self.client.post(CREATE_TICKET_URL)
        self.assertEquals(response.status_code, 200)

    def test_create_ticket_view_saves_data(self):
        """Test that TicketCreateView saves valid object."""

        data = {
            'title': 'test ticket',
            'description': 'Error!',
            'importance': "LOW",
            'created_by': self.user.id, # Here I had to provide user's ID!
        }
        self.client.force_login(self.user)
        response = self.client.post(CREATE_TICKET_URL, data=data)
        self.assertTrue(Ticket.objects.filter(
            title='test ticket').exists())
