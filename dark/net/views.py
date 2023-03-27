# Create your views here.
from django.shortcuts import render
from net.models import Account, AccountEmail
from django.contrib.auth.models import User
from rest_framework import viewsets
from net.serializers import UserSerializer, AccountSerializer

def nick_show(request):
    accounts = Account.objects.all()

    return render(request, 'index.html', {'accounts': accounts})


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
