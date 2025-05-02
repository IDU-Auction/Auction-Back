from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import UserActivityLog
from django.utils.timezone import now

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    UserActivityLog.objects.create(
        user=user,
        action="login",
        ip_address=get_client_ip(request),
        timestamp=now()
    )

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    UserActivityLog.objects.create(
        user=user,
        action="logout",
        ip_address=get_client_ip(request),
        timestamp=now()
    )

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
