from django.contrib import admin
from .models import Destination, Lodging, Room, Booking
# Register your models here.

admin.site.register(Destination)
admin.site.register(Lodging)
admin.site.register(Room)
admin.site.register(Booking)
