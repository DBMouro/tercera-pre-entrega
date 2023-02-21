from django.urls import path
from . import views
urlpatterns = [
    path('users/', views.users, name='users'),
    path('users/details/<int:id>', views.user_details, name='user_details'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/find/', views.user_find, name='user_find'),
    path('warehouses/', views.warehouses, name='warehouses'),
    path('warehouses/details/<int:id>', views.warehouse_details, name='warehouse_details'),
    path('warehouses/create/', views.warehouse_create, name='warehouse_create'),
    path('warehouses/find/', views.warehouse_find, name='warehouse_find'),
    path('products/', views.products, name='products'),
    path('products/details/<int:id>', views.product_details, name='product_details'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/find/', views.product_find, name='product_find'),
]