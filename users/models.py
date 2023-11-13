from django.db import models


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    admin = models.BooleanField(default=False)
    active_from = models.DateTimeField()

