from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list-cities'),
    path('delete/<str:city_name>/', views.delete_city, name='delete_city'),
]