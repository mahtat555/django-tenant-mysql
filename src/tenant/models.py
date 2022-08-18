from django.db import models

class Client(models.Model):
    """ Representing the tenant client
    """

    name = models.CharField(max_length=100)
    db_name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Domain(models.Model):
    """ Representing the tenant domain
    """

    tenant = models.ForeignKey(Client, on_delete=models.CASCADE)
    domain = models.CharField(max_length=100)
    is_primary = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
