from rest_framework import serializers
from django.contrib.auth.models import User
from net.models import Account, AccountEmail, Game


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class AccountEmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccountEmail
        fields = ['id', 'email']


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'price', 'status', 'like', 'dislike']


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    email = AccountEmailSerializer()
    games = GameSerializer(many=True)

    class Meta:
        model = Account
        fields = ['url', 'nick', 'email', 'date', 'like', 'dislike', 'games']
