from django.conf.urls import url
from .views import charts, ChartData

urlpatterns = [
    url(r'^api/data$', ChartData.as_view()),
    url(r'^$', charts, name='charts'),
]