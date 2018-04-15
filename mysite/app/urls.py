from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('create-order', views.create_order, name='create-order'),
    path('order-details', views.order_details, name='order-details'),
]
