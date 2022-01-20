from django.urls import reverse
from tickets.models import Ticket
from tickets.forms import TicketForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class TicketCreateView(LoginRequiredMixin, CreateView):
    """Class based view for creating a Ticket."""

    form_class = TicketForm
    template_name = 'tickets/create_ticket.html'
    model = Ticket

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TicketCreateView, self).form_valid(form)


