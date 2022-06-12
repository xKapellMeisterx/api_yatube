from django.urls import path, include
from rest_framework import routers

from .views import posts_list

urlpatterns = [
   path('posts/', posts_list),
]



















# router = routers.DefaultRouter()
# router.registry('api/v1/posts', cat_list)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]