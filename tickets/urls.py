from django.urls import path
from tickets.views import TicketCreateView


app_name = 'tickets'


urlpatterns = [
    path('create-ticket/', TicketCreateView.as_view(), name='create-ticket'),
]