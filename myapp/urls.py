from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('products/', views.products, name='products'),
    path('student/', views.student, name='student'),
    path('calculator/', views.calculator, name='calculator'),
]
