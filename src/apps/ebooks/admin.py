from django.contrib import admin

from tenant.core.admin import TenantAdmin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(TenantAdmin):
    """ Add the Book model to admin page
    """
    list_display = ("book", "start", "end", "duration")
