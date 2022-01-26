from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from users.forms import CustomUserCreationForm, CustomUserAuthenticationForm
from tickets.forms import TicketForm
from tickets.models import Ticket


TICKET_FORM_URL = reverse('tickets:ticket-create')


class CustomUserCreationFormTest(TestCase):
    """Test case for custom user creation and authentication forms."""
    pass


class TicketFormTest(TestCase):
    """Test case for Ticket form."""
    
    def setUp(self):

        self.client = Client()
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            full_name='Tester Tester',
            password='test123!',
        )
    
    def test_form_is_valid_object_created(self):
        """Test that data is passed into form and object is created."""
        
        data = {
            'title': 'test ticket',
            'description': 'Error!',
            'importance': "LOW",
        }
        self.client.force_login(self.user)
        form = TicketForm(data=data)
        form.instance.created_by = self.user
        self.assertTrue(form.is_valid())
        form.is_valid()
        form.save()
        self.assertTrue(Ticket.objects.filter(title='test ticket').exists())

