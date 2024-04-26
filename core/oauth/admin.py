# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (
    ApplicationClient,
    ClientSecret,
    AuthorizationCode,
)


class ApplicationClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'client_id', 'user', 'created_at']
    readonly_fields = ['client_id', 'created_at']
    search_fields = ['name', 'client_id', 'user__email']
    list_filter = ['created_at', 'user']

admin.site.register(ApplicationClient, ApplicationClientAdmin)
admin.site.register(ClientSecret)
admin.site.register(AuthorizationCode)