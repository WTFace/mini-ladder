from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='canvas-home'),
    path('dari/', views.ladder),
    path('select/<int:id>', views.get_one),
    path('api/<int:id>', views.api),
    path('get_time', views.get_time)
]