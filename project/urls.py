from django.urls import path
from feed.views import HelloWorldView

urlpatterns = [
    path('', HelloWorldView.as_view(), name='hello_world'),
]
