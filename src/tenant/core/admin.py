from django.contrib import admin

from .urls import tenant_db_from_request
from .settings import SHARED_APPS, TENANT_APPS


class TenantAdmin(admin.ModelAdmin):
    """ Managing the Admin tenants
    """

    def has_view_permission(self, request, obj=None):
        if self._check_permission(request):
            return super().has_view_permission(request, obj)
        return False

    def has_add_permission(self, request):
        if self._check_permission(request):
            return super().has_add_permission(request)
        return False

    def has_change_permission(self, request, obj=None):
        if self._check_permission(request):
            return super().has_change_permission(request, obj)
        return False

    def has_delete_permission(self, request, obj=None):
        if self._check_permission(request):
            return super().has_delete_permission(request, obj)
        return False

    def _check_permission(self, request):
        db_name = tenant_db_from_request(request)
        app_name = self.model._meta.app_label

        if db_name is None:
            if app_name in SHARED_APPS:
                return True
        else:
            if app_name in TENANT_APPS:
                return True
        return False
