""" Dajngo routers,
Used for handling multiple databases
"""

from django.conf import settings
from .middlewares import get_current_db_name


class TenantRouter:
    """ Tenat routers
    """

    def db_for_read(self, model, **hints):
        return self._filter(model)

    def db_for_write(self, model, **hints):
        return self._filter(model)

    def allow_relation(self, *args, **kwargs):
        return True

    def allow_syncdb(self, *args, **kwargs):
        return None

    def allow_migrate(self, *args, **kwargs):
        return None

    def _filter(self, model):
        """ Get the model table """

        shared_apps = [app.split(".")[-1] for app in settings.SHARED_APPS]
        tenant_apps = [app.split(".")[-1] for app in settings.TENANT_APPS]

        app_name = model._meta.app_label
        db_name = get_current_db_name()

        if db_name and app_name in tenant_apps:
            return db_name

        if app_name in shared_apps:
            return "default"

        if app_name not in shared_apps:
            raise Exception(f"No table found for {app_name}")

        return "default"
