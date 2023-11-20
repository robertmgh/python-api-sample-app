from django.urls import path

from . import views

urlpatterns = [
    path("", views.UserList.as_view(), name="users.details"),
    path("<int:pk>/", views.UserDetails.as_view())
]
