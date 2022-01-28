from django.urls import path
from users.views import CreateCustomUserApiView


app_name = 'api'


urlpatterns = [
    path('register-user/', CreateCustomUserApiView.as_view(), name='register-user'),
]