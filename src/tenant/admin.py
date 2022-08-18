from django.contrib import admin

from .models import Client, Domain

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'db_name')


@admin.register(Domain)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'domain', 'is_primary')
