from django.core.management.base import BaseCommand
from net.models import Account, AccountEmail
from django.db.models import Q, F


class Command(BaseCommand):
    help = 'Хелп'

    def handle(self, *args, **options):
        my_function()


def my_function():
    print(Account.objects.filter().order_by(-F('like'))) # ;)
