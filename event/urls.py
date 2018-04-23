from django.urls import path

from event import views

app_name = 'event'
urlpatterns = [
    path('new/', views.create),
    path('thanks/', views.thanks, name='thanks'),
    path('<int:event_id>/', views.details, name='details'),
    path('<int:event_id>/respond/<str:invite_id>/', views.invitation, name='invitation'),
    path('<int:event_id>/respond/<str:invite_id>/<str:response>/', views.respond, name='respond'),
]