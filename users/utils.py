import pyotp
import qrcode
from io import BytesIO
import base64

def generate_otp_secret():
    return pyotp.random_base32()

def get_totp_uri(user, secret):
    return pyotp.totp.TOTP(secret).provisioning_uri(name=user.username, issuer_name="Auction Platform")

def generate_qr_code_image(uri):
    qr = qrcode.make(uri)
    buffer = BytesIO()
    qr.save(buffer, format='PNG')
    return base64.b64encode(buffer.getvalue()).decode()
