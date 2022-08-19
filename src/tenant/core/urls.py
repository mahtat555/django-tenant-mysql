from ..models import Domain


def hostname_from_request(request):
    return request.get_host().split(':')[0].lower()


def tenant_db_from_request(request):
    hostname = hostname_from_request(request)

    # Check if subdomain exists
    domain = Domain.objects.filter(domain=hostname)
    if not domain.exists():
        return None

    return domain.first().tenant.db_name
