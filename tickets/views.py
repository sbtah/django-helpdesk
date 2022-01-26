from tickets.forms import TicketForm
from tickets.models import Ticket
# For CBV
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class TicketListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """List all tickets view."""

    model = Ticket
    template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'
    

    def get_queryset(self, *args, **kwargs):
        queryset = super(TicketListView, self).get_queryset(*args, **kwargs)
        queryset = queryset.order_by("-created")
        return queryset

    def test_func(self):
        return self.request.user.is_staff


class PersonalTicketListView(LoginRequiredMixin, ListView):
    """List all tickets created by logged user."""

    model = Ticket
    template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        """Get queryset for of tickets for current logged user."""
        queryset = super(PersonalTicketListView, self).get_queryset()
        queryset = queryset.filter(
            created_by=self.request.user
        ).order_by("-created")
        return queryset


class TicketDetailView(LoginRequiredMixin, DetailView):
    """Detail view for ticket."""

    model = Ticket
    template_name = 'tickets/ticket_details.html'
    context_object_name = 'ticket'
    permission_required = 'is_staff'


class TicketCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Class based view for creating a Ticket."""

    form_class = TicketForm
    template_name = 'tickets/ticket_create.html'
    success_message = 'Ticket created, thank you'
    model = Ticket

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        """Custom form valid for adding created_by field as a currently logged user."""
        form.instance.created_by = self.request.user
        return super(TicketCreateView, self).form_valid(form)