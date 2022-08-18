from django.contrib import admin

from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """ Add the Book model to admin page
    """
    list_display = ("book", "start", "end", "duration")
