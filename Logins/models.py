from django.db import models


# Create your models here.
class Loginmodels(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.TextField(max_length=120, null=False)
    password = models.TextField(max_length=120, null=False)
    email = models.TextField(max_length=120, null=False)
    fullname = models.TextField(max_length=120, null=True)
    address = models.TextField(max_length=255, null=True)
