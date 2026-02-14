from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('car/add/', views.car_create, name='car_create'),
    path('register/', views.register, name='register'),
    path('inbox/', views.inbox, name='inbox'),
    path('car/<int:car_id>/contact/', views.send_message, name='send_message'),
    path('car/<int:car_id>/order/', views.place_order, name='place_order'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    path('car/<int:car_id>/validate/', views.validate_car, name='validate_car'),
]