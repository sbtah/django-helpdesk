from tickets.models import Ticket
from django import forms
from django.utils.translation import gettext_lazy as _

class TicketForm(forms.ModelForm):
    """A model for creating a ticket."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['screenshot'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['importance'].widget.attrs.update(
            {'class': 'form-control'})
   
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'screenshot', 'importance', 'created_by',]
        help_texts = {
            'title': _('Short useful title.'),
            'description': _('WHEN, HOW, SOFTWARE, HARDWARE?'),
            'screenshot': _('Post a screenshot of error.'),
            'importance': _("LOW:It's anoying, MID:It slows me down, HIGH: I can't work, VERY HIGH: Critical (like server is burning)"),
        } 