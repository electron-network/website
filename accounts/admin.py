from django.contrib import admin

from accounts.models import Signup


@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'opt_out', ]
    list_filter = ['opt_out', ]
    search_fields = ['email', ]
