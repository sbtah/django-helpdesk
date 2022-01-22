from tickets.forms import TicketForm
from tickets.models import Ticket
# For CBV
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class TicketCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Class based view for creating a Ticket."""

    form_class = TicketForm
    template_name = 'tickets/create_ticket.html'
    success_message = 'Ticket created, thank you'
    model = Ticket

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        """Custom form valid for adding created_by as a currently logged user."""
        form.instance.created_by = self.request.user
        return super(TicketCreateView, self).form_valid(form)