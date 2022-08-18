from django.db import models


class Reservation(models.Model):

    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def duration(self):
        return self.end - self.start
