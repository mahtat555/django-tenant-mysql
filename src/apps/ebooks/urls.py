from django.urls import path, include
from rest_framework import routers

from .views import ReservationView, ReservationBookView


router = routers.DefaultRouter()
router.register(r'', ReservationView, 'reservation')


urlpatterns = [
    path('', include(router.urls)),
    path('<int:reservation_id>/book',
         ReservationBookView.as_view(), name="reservation-book"),
]
