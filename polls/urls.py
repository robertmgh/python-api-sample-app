from django.urls import include, path

from rest_framework import routers

from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path("", include(router.urls))
    #path("<int:user_id>/", views.detail, name="detail"),
]
