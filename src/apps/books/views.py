from rest_framework.viewsets import ModelViewSet

from .serializers import BookSerializer
from .models import Book


class BookView(ModelViewSet):
    """ Handling the books
    """

    serializer_class = BookSerializer
    queryset = Book.objects.all()
