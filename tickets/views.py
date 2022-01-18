from django.shortcuts import render, redirect
from tickets.models import Ticket
from tickets.forms import TicketForm


def create_ticket(request):
    """Create a ticket view."""

    form = TicketForm
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(request, 'tickets/create_ticket.html' , {
        'form' : form,
    })