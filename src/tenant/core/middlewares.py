import threading
from django.conf import settings

from .urls import tenant_db_from_request
from saas.settings import ROOT_URLCONF, PUBLIC_URLCONF

THREAD_LOCAL = threading.local()


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        db = tenant_db_from_request(request)

        if db is None:
            settings.ROOT_URLCONF = PUBLIC_URLCONF
        else:
            settings.ROOT_URLCONF = ROOT_URLCONF

        setattr(THREAD_LOCAL, "DB", db)
        response = self.get_response(request)
        return response


def get_current_db_name():
    return getattr(THREAD_LOCAL, "DB", None)


def set_db_for_router(db):
    setattr(THREAD_LOCAL, "DB", db)
