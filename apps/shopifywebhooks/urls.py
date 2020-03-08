from django.urls import path

from . import views

urlpatterns = [
    path('product/update', views.product_update_or_create),
    path('product/create', views.product_update_or_create),
    path('order/update', views.order_update_or_create),
    path('order/create', views.order_update_or_create),
]