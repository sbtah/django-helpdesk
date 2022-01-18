from django.urls import path
from tickets.views import create_ticket

app_name = 'tickets'


urlpatterns = [
    path('create-ticket/', create_ticket, name='create-ticket'),
]