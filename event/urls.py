from django.urls import path

from event import views

urlpatterns = [
    path('new/', views.create),
]