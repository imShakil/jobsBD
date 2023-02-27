from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.openning, name='job finding'),
]

