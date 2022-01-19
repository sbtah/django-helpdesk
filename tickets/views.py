from django.shortcuts import render, redirect
from django.urls import reverse
from tickets.models import Ticket
from tickets.forms import TicketForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class TicketCreateView(CreateView):
    """Class based view for creating a Ticket."""

    form_class = TicketForm
    template_name = 'tickets/create_ticket.html'
    queryset = Ticket.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        super().form_valid(form)

    def get_success_url(self):
        return reverse('home')
