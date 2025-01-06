from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard1, name='dashboard1'),
    path('addfood/', views.addfood, name='addfood'),
    path('edit/<int:food_id>/', views.update_food, name='editprod'),
    path('delete/<int:food_id>/', views.delete_food, name='delete_food'),
    path('delete_all_food/', views.delete_all_food, name='delete_all_food'),

]
