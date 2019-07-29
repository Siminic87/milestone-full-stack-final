from django.conf.urls import url
from .views import get_all

urlpatterns = [
    url(r'^$', get_all, name='get_all'),
]