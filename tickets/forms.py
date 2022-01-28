from tickets.models import Ticket
from django import forms
from django.utils.translation import gettext_lazy as _


class TicketCreateForm(forms.ModelForm):
    """A model form for creating a ticket."""

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
        fields = ['title', 'description', 'screenshot', 'importance']


# This form is not tested yet!
class TicketStaffUpdateForm(forms.ModelForm):
    """A model form for updating a ticket with staff users."""

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
        self.fields['created_by'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['status'].widget.attrs.update(
            {'class': 'form-control'})

    class Meta:
        model = Ticket
        fields = "__all__"