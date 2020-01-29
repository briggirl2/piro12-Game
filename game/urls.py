
from django.urls import path, include

from game import views

urlpatterns = [
    path('', views.home, name='home')
]
