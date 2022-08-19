from django.urls import path, include
from rest_framework import routers

from .views import BookView


router = routers.DefaultRouter()
router.register(r'', BookView, 'books')


urlpatterns = [
    path('', include(router.urls)),
]
