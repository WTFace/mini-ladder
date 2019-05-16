from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='canvas-home'),
    path('dari/', views.ladder),
]