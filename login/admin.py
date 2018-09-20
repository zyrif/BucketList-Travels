from django.contrib import admin
from .models import UsersModel

# Register your models here.


class UsersModelAdmin(admin.ModelAdmin):
    list_display = ('userid', 'name', 'email', 'contactno', 'adminstatus')


admin.site.register(UsersModel, UsersModelAdmin)
