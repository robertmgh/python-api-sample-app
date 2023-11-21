from django.db import models


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    admin = models.BooleanField(default=False)
    active_from = models.DateTimeField()
    
class AccessGroup(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        User,
        through="AccessMembership",
        through_fields=("access_group", "user"),
    )


class AccessMembership(models.Model):
    id = models.BigIntegerField(primary_key=True)
    access_group = models.ForeignKey(AccessGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="access_membership_invites",
    )
    invite_data = models.DateTimeField(auto_now_add=True)

