from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:recipe_id>/", views.recipeView, name="detail"),
    path("search/", views.searchView, name="search"),
    path("<str:category>/", views.categoryView, name="category"),
]
