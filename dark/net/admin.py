from django.contrib import admin
from net.models import User, Account, AccountEmail

# Register your models here.
@admin.register(User)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('nick', 'password', 'email')
    search_fields = ('nick',)


@admin.register(Account)
class SettingAccount(admin.ModelAdmin):
    list_display = ('nick', 'password', 'email')
    search_fields = ('nick',)


@admin.register(AccountEmail)
class SettingAccountEmail(admin.ModelAdmin):
    list_display = ('email', 'adress', 'password', 'port', 'status')
    search_fields = ('symbol',)
