from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_3D, name='home_3D'),
    path('run', views.run_3D, name='run_3D')
]
