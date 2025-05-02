from django.shortcuts import render
from .models import TwoFactorAuth
from .utils import generate_otp_secret, get_totp_uri, generate_qr_code_image
from django.contrib.auth.decorators import login_required

@login_required
def enable_2fa(request):
    user = request.user
    if request.method == 'POST':
        secret = generate_otp_secret()
        tfa, created = TwoFactorAuth.objects.get_or_create(user=user)
        tfa.secret_key = secret
        tfa.is_enabled = True
        tfa.save()
        return render(request, 'users/2fa_enabled.html')
    else:
        secret = generate_otp_secret()
        uri = get_totp_uri(user, secret)
        qr_image = generate_qr_code_image(uri)
        return render(request, 'users/enable_2fa.html', {'qr_code': qr_image, 'secret': secret})
