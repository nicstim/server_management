from django.contrib import admin

from .models import VPS


@admin.register(VPS)
class VPSAdmin(admin.ModelAdmin):
    ...
