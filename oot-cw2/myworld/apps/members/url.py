from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('add/', views.add, name='add'),
    path('book/', views.book, name='book'),
    path('eraser/', views.eraser, name='eraser'),
    path('glue/', views.glue, name='glue'),
    path('login/', views.login, name='login'),
    path('pen/', views.pen, name='pen'),
    path('remove/', views.remove, name='remove'),
    path('scissors/', views.scissors, name='scissors'),
    path('search/', views.search, name='search'),
]