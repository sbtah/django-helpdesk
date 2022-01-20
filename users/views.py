from users.forms import CustomUserAuthenticationForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy


class LoginCustomUserView(SuccessMessageMixin, LoginView):
    """Class based view for login in users."""
    
    authentication_form = CustomUserAuthenticationForm
    template_name = 'users/login_user.html'
    next_page = 'home'
    success_message = "Your are logged in"


class LogoutCustomUserView(SuccessMessageMixin, LogoutView):
    """Class based view to logout users."""

    template_name = 'users/logout_user.html'
    success_url = reverse_lazy('home')
    success_message = "Your are logged out"


class CreateCustomUserView(SuccessMessageMixin, CreateView):
    """Class based view for creating new users."""

    template_name = 'users/create_user.html'
    success_url = reverse_lazy('users:login-user')
    form_class = CustomUserCreationForm
    success_message = "Your profile was created successfully"

