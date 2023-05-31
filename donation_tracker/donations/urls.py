from django.urls import path
from . import views

urlpatterns = [
    path('bitcoin_price/', views.bitcoin_price, name='bitcoin_price'),
]
