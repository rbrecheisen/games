from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('phaser', views.phaser, name='phaser'),
    path('tankbatallion', views.tankbatallion, name='tankbatallion'),
]
