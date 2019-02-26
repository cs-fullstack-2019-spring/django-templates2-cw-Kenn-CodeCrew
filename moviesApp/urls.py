from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('synopsis/<int:movieID>', views.synopsis, name="synopsis"),
    path('details/<int:movieID>', views.details, name="details"),
]