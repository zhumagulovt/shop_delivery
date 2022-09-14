from django.urls import path

from . import views

urlpatterns = [
    path('', views.TestNotification.as_view())
]