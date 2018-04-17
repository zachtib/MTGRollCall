from django.urls import path

from event import views

urlpatterns = [
    path('new/', views.create),
    path('<int:event_id>/respond/<str:invite_id>/<int:user_id>/', views.respond),
]