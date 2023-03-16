from django.core.management.base import BaseCommand
from net.models import Account, AccountEmail


class Command(BaseCommand):
    help = 'Хелп'

    def handle(self, *args, **options):
        my_function()


def my_function():
    for account in Account.objects.all():
        print(account)
