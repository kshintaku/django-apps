from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<str:city>/', views.spec_city, name='index'),
  # path('input-search/', views.search_city, name='index'),
]