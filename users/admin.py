from django.contrib import admin
from .models import CustomUser, Role, TwoFactorAuth, UserActivityLog
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Role)
admin.site.register(TwoFactorAuth)
admin.site.register(UserActivityLog)
