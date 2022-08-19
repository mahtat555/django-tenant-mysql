# pylint:disable=import-error

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.books.serializers import BookSerializer
from .serializers import ReservationSerializer
from .models import Reservation


class ReservationView(ModelViewSet):
    """ Handling the reservations
    """

    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()


class ReservationBookView(APIView):
    def get(self, request, reservation_id):
        try:
            reservation = Reservation.objects.get(pk=reservation_id)
        except Reservation.DoesNotExist:
            return Response({
                "error": f"No reservation with this ID {reservation_id}"
            }, status=404)

        serializer = BookSerializer(reservation.book)
        return Response(serializer.data)
