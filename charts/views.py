from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from datetime import timedelta
from posts.models import Post, Voter

### Summary Charts ###
class ChartData(APIView):
    """
    View to query database for average of bugs and feature requests that have 
    been "done" per day, week and month in last month. 
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ['Day', 'Week', 'Month']
        default_items = [Post.objects.filter(type="Feature Request", status="Done", published_date__gte=timezone.now()-timedelta(30)).count() / 30,
                        Post.objects.filter(type="Feature Request", status="Done", published_date__gte=timezone.now()-timedelta(28)).count() / 4,
                        Post.objects.filter(type="Feature Request", status="Done", published_date__gte=timezone.now()-timedelta(30)).count()]
        default_items2 = [Post.objects.filter(type="Bug", status="Done", published_date__gte=timezone.now()-timedelta(30)).count() / 30,
                        Post.objects.filter(type="Bug", status="Done", published_date__gte=timezone.now()-timedelta(28)).count() / 4,
                        Post.objects.filter(type="Bug", status="Done", published_date__gte=timezone.now()-timedelta(30)).count()]
        data = {
            "labels": labels,
            "default": default_items,
            "default2": default_items2,
        }
        return Response(data)

def charts(request):
    """
    Renders page with summary charts
    """
    return render(request, 'charts.html')