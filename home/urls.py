from django.urls import path
from login.views import loginView, signupView
from .views import index

urlpatterns = [
    path('', index, name='homepage'),
    path('login', loginView, name='loginpage'),
    path('signup', signupView, name='signuppage'),
]
