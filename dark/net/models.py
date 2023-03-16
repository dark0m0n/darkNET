from django.db import models

# Create your models here.
class User(models.Model):
    nick = models.CharField(max_length=33)
    password = models.CharField(max_length=66)
    email = models.CharField(max_length=100)


class AccountEmail(models.Model):
    email = models.CharField(max_length=100)
    adress = models.CharField(max_length=30)
    port = models.IntegerField()
    password = models.CharField(max_length=66)
    status = models.BooleanField()

    def __str__(self) -> str:
        return self.email


class Account(models.Model):
    nick = models.CharField(max_length=255)
    password = models.CharField(max_length=66)
    email = models.ForeignKey(AccountEmail, on_delete=models.CASCADE)
