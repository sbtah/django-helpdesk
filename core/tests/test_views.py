from math import perm
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from tickets.models import Ticket


CREATE_TICKET_URL = reverse('tickets:ticket-create')
LIST_TICKET_URL = reverse('tickets:ticket-list')


class TestTicketCreateView(TestCase):
    """Test case for TicketCreateView."""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            password='test1231',
        )
        self.factory = RequestFactory() # Use this for test in Create
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


class TestTicketListView(TestCase):
    """Test case for TicketListView"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            password='test1231',
        )
        self.staff_user = get_user_model().objects.create_user(
            email='admin@admin.com',
            password='test123!',
            is_staff=True,
        )

        self.data = Ticket.objects.create(
            title='Error',
            description='Something is not working',
            importance='LOW',
            created_by=self.user,
            status='CREATED',
            created='2022-01-22',
            updated='2022-01-22',
        )
        self.client = Client()
        self.factory = RequestFactory()
    
    def test_list_ticket_view_without_user(self):
        """Test the url of ticket list view without logged user."""
        response = self.client.get(LIST_TICKET_URL)
        self.assertEquals(response.status_code, 302)
        # self.assertInHTML('<h2>LOGIN</h2>', html)
    
    def test_list_ticket_view_for_user_without_permission(self):
        """Test the url of view with user that doesn't have the proper permissions."""
        self.client.force_login(self.user)
        response = self.client.get(LIST_TICKET_URL)
        self.assertEquals(response.status_code, 403)

    def test_list_ticket_view_for_user_with_permission(self):
        """Test the url of view with user that have the proper permission."""
        self.client.force_login(self.staff_user)
        response = self.client.get(LIST_TICKET_URL)
        self.assertEquals(response.status_code, 200)

    def test_that_list_ticket_view_lists_data(self):
        """Test that view outputs proper data."""
        self.client.force_login(self.staff_user)
        response = self.client.get(LIST_TICKET_URL)
        self.assertEqual(len(response.context['object_list']), 1)