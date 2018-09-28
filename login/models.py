from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contactno = models.CharField(max_length=20, unique=True)
    # add ticket info, profile pic and stuff here

    def __str__(self):
        return self.user.username
