from django.urls import path
from net.views import nick_show

urlpatterns = [
    path("", nick_show)
]
