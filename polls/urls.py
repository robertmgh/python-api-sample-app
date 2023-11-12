from django.urls import include, path

from rest_framework import routers

from . import views

urlpatterns = [
    path("users/", views.UserList.as_view())
    #path("<int:user_id>/", views.detail, name="detail"),
]
