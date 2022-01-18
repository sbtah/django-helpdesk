from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Ticket(models.Model):
    """Model for user's tickets."""

    
    class Importance(models.TextChoices):
        low = "LOW"
        mid = "MID"
        high = "HIGH"
        very_high = "VERY HIGH"
    
    class Status(models.TextChoices):
        created = 'CREATED'
        picked_up = 'PICKED UP'
        extended = 'EXTENDED'
        finished = 'FINISHED'


    title = models.CharField(help_text=_('Title of problem'), max_length=100)
    description = models.TextField(help_text=_('Description of problem.'))
    screenshot = models.FileField(upload_to='worksheets')
    importance = models.CharField(max_length=20, choices=Importance.choices)
    created_by = models.CharField(max_length=20)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.created
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('tickets:ticket-details', args=[self.id])
    
    def __str__(self):
        return f"ID:{self.id} Title:{self.title} Created by:{self.created_by} Status:{self.status}"
