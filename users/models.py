from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50)  # Admin, User, Moderator

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    # GDPR: maxfiylikka ruxsat berilgan foydalanuvchi
    consent_given = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class TwoFactorAuth(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_enabled = models.BooleanField(default=False)
    secret_key = models.CharField(max_length=255, blank=True, null=True)  # Google Authenticator bilan ishlash uchun

    def __str__(self):
        return f"2FA for {self.user.username}"
    
class UserActivityLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)  # example: login, logout, update_profile
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"

