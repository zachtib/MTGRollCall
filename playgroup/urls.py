from django.urls import path

from playgroup import views

app_name = 'playgroup'
urlpatterns = [
    path('', views.dashboard, name='home'),
    path('create/', views.create, name="create"),
    path('<int:group_id>/', views.details, name="details"),
]
