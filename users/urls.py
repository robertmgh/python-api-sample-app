from django.urls import path

from . import views

urlpatterns = [
    path("users/", views.UserList.as_view(), name="users.details"),
    path("users/<int:pk>/", views.UserDetails.as_view()),
    path("users/<int:pk>/access-groups", views.AccessMembershipList.as_view()),
    path("access-groups/", views.AccessGroupList.as_view())
]
