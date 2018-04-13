from django.urls import path

from playgroup import views

urlpatterns = [
    path('new/', views.create),
    path('', views.dashboard),
]