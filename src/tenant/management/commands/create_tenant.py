
from django.core.management.commands.migrate import Command as MigrationCommand

from tenant.models import Client, Domain
from ._core import get_migration_db


class Command(MigrationCommand):

    def handle(self, *args, **options):

        # Create the Tenant
        name = input("Name: ")
        db_name = input("Database Name: ")

        tenant = Client.objects.create(name=name, db_name=db_name)

        # Run the migrations
        options['database'] = db_name
        for app in get_migration_db(db_name):
            options['app_label'] = app
            super(Command, self).handle(*args, **options)

        # Create the domain
        domain = input("Domain Name: ")
        is_primary = input("Is Primary: ") or True

        Domain.objects.create(
            tenant=tenant, domain=domain, is_primary=is_primary
        )
