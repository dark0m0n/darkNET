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
    nick = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=66)
    email = models.ForeignKey(AccountEmail, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    games = models.ManyToManyField('Game')

    def __str__(self) -> str:
        return self.nick


class Game(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField()
    price = models.FloatField()
    like = models.PositiveIntegerField()
    dislike = models.PositiveIntegerField()
    changes = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.changes += 1

        return super().save(*args, **kwargs)      
