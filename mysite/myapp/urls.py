from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('food/', views.index, name='index'),
    path('delete/<int:pk>/', views.DeleteFoodView.as_view(), name='delete_food')

]
