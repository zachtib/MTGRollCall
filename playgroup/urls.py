from django.urls import path

from playgroup import views

app_name = 'playgroup'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create, name="create"),
    path('<int:group_id>/', views.details, name="details"),
    path('<int:group_id>/', views.edit, name="edit"),
    path('<int:group_id>/newevent/', views.newevent, name="newevent"),
]
