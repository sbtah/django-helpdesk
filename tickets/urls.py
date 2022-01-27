from django.urls import path
from tickets.views import TicketListView, PersonalTicketListView, TicketCreateView, TicketDetailView, TicketDeleteView


app_name = 'tickets'


urlpatterns = [
    path('ticket-list/', TicketListView.as_view(), name='ticket-list'),
    path('my-tickets/', PersonalTicketListView.as_view(), name='my-tickets'),
    path('ticket-create/', TicketCreateView.as_view(), name='ticket-create'),
    path('<int:pk>/', TicketDetailView.as_view(), name="ticket-details"),
    path('<int:pk>/delete/', TicketDeleteView.as_view(), name="ticket-delete"),
]