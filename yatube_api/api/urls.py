from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.registry('api/v1/posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
