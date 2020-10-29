from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name='product'),
    path('contact/', views.contact, name='contact'),
    path('', views.main, name='main')
    ]