from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),

    path('balance-check/', views.checkBalance, name='checkBalance'),
    path('balance-update/', views.addBalance, name='addBalance')
]