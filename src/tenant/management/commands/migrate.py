
from django.core.management.commands.migrate import Command as MigrationCommand
from django.db.utils import OperationalError

from tenant.models import Client
from ._core import get_migration_db


class Command(MigrationCommand):

    def handle(self, *args, **options):

        try:
            databases = [tenant.db_name for tenant in Client.objects.all()]
        except OperationalError:
            databases = []

        databases = ["default"] + databases

        for db_name in databases:
            options['database'] = db_name
            for app in get_migration_db(db_name):
                options['app_label'] = app
                super(Command, self).handle(*args, **options)
