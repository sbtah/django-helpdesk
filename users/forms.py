from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField


class CustomUserCreationForm(UserCreationForm):
    """Form for creating custom user model."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['full_name'].widget.attrs.update(
            {'class': 'form-control'})

    class Meta:
        model = get_user_model()
        fields = "__all__"
        field_classes = {'email': UsernameField}


class CustomUserChangeForm(UserChangeForm):
    """Form for changing custom user's data."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['full_name'].widget.attrs.update(
            {'class': 'form-control'})

    class Meta:
        model = get_user_model()
        fields = "__all__"
        field_classes = {'email': UsernameField}


class CustomUserAuthenticationForm(AuthenticationForm):
    """Form for authenticating custom users."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control'})
            
    class Meta:
        model = get_user_model()
        fields = "__all__"
        field_classes = {'email': UsernameField}