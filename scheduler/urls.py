from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("schedule", views.cal_form, name="calendar"),
]
