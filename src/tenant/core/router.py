""" Dajngo routers,
Used for handling multiple databases
"""

from .settings import SHARED_APPS, TENANT_APPS
from .middlewares import get_current_db_name


class TenantRouter:
    """ Tenat routers
    """

    def db_for_read(self, model, **hints):
        return self._get_current_db_name(model)

    def db_for_write(self, model, **hints):
        return self._get_current_db_name(model)

    def allow_relation(self, *args, **kwargs):
        return True

    def allow_syncdb(self, *args, **kwargs):
        return None

    def allow_migrate(self, *args, **kwargs):
        return None

    def _get_current_db_name(self, model):
        """ Get the model table """

        app_name = model._meta.app_label
        db_name = get_current_db_name()

        if db_name and app_name in TENANT_APPS:
            return db_name

        if app_name in SHARED_APPS:
            return "default"

        if app_name not in SHARED_APPS:
            raise Exception(f"No table found for {app_name}")

        return "default"
