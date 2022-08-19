from io import StringIO
from django.core.management import call_command
from django.conf import settings


def get_migration_db(db_name):

    apps = settings.TENANT_APPS
    if db_name == "default":
        apps = settings.SHARED_APPS

    apps = [app.split(".")[-1] for app in apps]

    result = set()
    out = StringIO()
    call_command(
        'showmigrations', f'--database={db_name}', format="plan", stdout=out
    )
    out.seek(0)
    for line in out.readlines():
        status, name = line.rsplit(' ', 1)

        name = name.strip().split(".")[0]
        status = status.strip() == '[X]'

        if name in apps and not status:
            result.add(name)

    return list(result)
