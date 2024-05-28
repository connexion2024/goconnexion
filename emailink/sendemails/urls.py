from django.urls import path

from . import views

urlpatterns = [
    path("valider/", views.submit_event, name="submit_event"),
    path("", views.index, name="index"),
]