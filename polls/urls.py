from django.urls import include, path

from rest_framework import routers

from . import views

urlpatterns = [
    path("users/", views.UserList.as_view()),
    path("<int:pk>/", views.UserDetails.as_view())
]
