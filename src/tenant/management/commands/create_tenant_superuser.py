from django.contrib.auth.management.commands.createsuperuser import (
    Command as SuperUserCommand
)

from tenant.models import Client


class Command(SuperUserCommand):
    """ Create the superuser for the a specific tenant
    """

    def handle(self, *args, **options):
        tenants = Client.objects.all()
        options['database'] = self._get_db_name(tenants)
        super(Command, self).handle(*args, **options)

    def _list_databases(self, tenants):
        for tenant in tenants:
            for domain in tenant.domain_set.all():
                print(f"{tenant.db_name} - {domain.domain}")

    def _get_db_name(self, tenants):
        db_name = input(
            "Enter Database Name ('?' to list databases): ").strip()

        if db_name == "?":
            self._list_databases(tenants)
            return self._get_db_name(tenants)

        if not tenants.filter(db_name=db_name).exists():
            print("Database name not found !!")
            return self._get_db_name(tenants)

        return db_name
