from django.contrib import admin

from tenant.core.admin import TenantAdmin
from .models import Book


@admin.register(Book)
class BookAdmin(TenantAdmin):
    """ Add the Book model to admin page
    """
    list_display = ("name", "description", "price")
