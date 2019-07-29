from django.conf.urls import url
from .views import get_all, get_features, get_bugs, post_detail, create_or_edit_post, upvote, about, delete_post

urlpatterns = [
    url(r'^$', get_all, name='get_all'),
    url(r'^features/$', get_features, name='get_features'),
    url(r'^bugs/$', get_bugs, name='get_bugs'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_or_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post'),
    url(r'^upvote/(?P<post_id>[0-9]+)/$', upvote, name='upvote'),
    url(r'^about/$', about, name='about'),
    url(r'^(?P<pk>\d+)/delete/$', delete_post, name='delete_post'),
]