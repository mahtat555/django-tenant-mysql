from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """ Add the Book model to admin page
    """
    list_display = ("name", "description", "price")
