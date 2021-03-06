"""tms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import index, profileView, ProcessBooking, GetDestinations
from home.views import SearchView, SelectionView, BookingView
from login.views import loginView, signupView, logoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='homepage'),
    path('login', loginView, name='loginpage'),
    path('signup', signupView, name='signuppage'),
    path('profile', profileView, name='profilepage'),
    path('search', SearchView.as_view(), name='searchpage'),
    path('selection', SelectionView.as_view(), name='selectionpage'),
    path('booking', BookingView.as_view(), name='bookingpage'),
    path('ajax/processbooking', ProcessBooking, name='processbooking'),
    path('ajax/getdestinations', GetDestinations, name='getdestinations'),
    path('logout', logoutView, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
