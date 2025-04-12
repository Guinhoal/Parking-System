from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard.html', views.dashboard, name='dashboard'),
    path('car_entry/', views.car_entry, name='car_entry'),
    path('car-exit/', views.car_exit, name='car_exit'),
    path('car-list/', views.car_list, name='car_list'),
    path('car_entry.html', views.car_entry, name='car_entry'),
    path('car-exit.html', views.car_exit, name='car_exit'),
    path('car-list.html', views.car_list, name='car_list'),
    path('car-list.html', views.car_list, name='car_list'),
    path('car-payment/<int:pk>/', views.car_payment, name='car_payment'),
    path('car-history/', views.car_history, name='car_history'),
]
