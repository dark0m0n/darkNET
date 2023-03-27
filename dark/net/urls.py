from django.urls import path, include
from net.views import nick_show
from rest_framework import routers
from net.views import UserView, AccountView

router = routers.DefaultRouter()
router.register('users', UserView)
router.register('accounts', AccountView)

urlpatterns = [
    path("", include(router.urls)),
]
