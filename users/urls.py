from django.urls import path
from users.views import LoginCustomUserView, LogoutCustomUserView, CreateCustomUserView


app_name = 'users'


urlpatterns = [
    path('login/', LoginCustomUserView.as_view(), name='login-user'),
    path('logout/', LogoutCustomUserView.as_view(), name='logout-user'),
    path('register/', CreateCustomUserView.as_view(), name='register-user'),
]