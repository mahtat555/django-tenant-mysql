from django.conf import settings


SHARED_APPS = [app.split(".")[-1] for app in settings.SHARED_APPS]

TENANT_APPS = [app.split(".")[-1] for app in settings.TENANT_APPS]
