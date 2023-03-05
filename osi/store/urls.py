from django.urls import path
from . import views
from .views import product_detail



urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
]