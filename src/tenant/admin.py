from django.contrib import admin

from .models import Client, Domain
from .core.admin import TenantAdmin


@admin.register(Client)
class ClientAdmin(TenantAdmin):
    list_display = ('name', 'db_name')


@admin.register(Domain)
class DomainAdmin(TenantAdmin):
    list_display = ('tenant', 'domain', 'is_primary')
