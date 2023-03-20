# Create your views here.
from django.shortcuts import render
from net.models import Account, AccountEmail

def nick_show(request):
    accounts = Account.objects.all()

    return render(request, 'index.html', {'accounts': accounts})
