from django.conf.urls import url
from .views import get_all, get_features, get_bugs, post_detail

urlpatterns = [
    url(r'^$', get_all, name='get_all'),
    url(r'^features/$', get_features, name='get_features'),
    url(r'^bugs/$', get_bugs, name='get_bugs'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
]