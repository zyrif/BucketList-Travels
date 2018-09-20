from django.db import models

# Create your models here.


class UsersModel(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)
    contactno = models.CharField(max_length=14, unique=True)
    adminstatus = models.BooleanField(default=False)

    def __str__(self):
        return str(self.userid)
