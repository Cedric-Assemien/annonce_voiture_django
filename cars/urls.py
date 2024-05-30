from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.car_detail, name='car_detail'),
    path('search', views.search, name='search'),
    path('cars1', views.car1, name='cars1'),
    path('maison_appart',views.maison_appart,name='maison'),
    path('terrain',views.terrain,name='terrain')
       
]
