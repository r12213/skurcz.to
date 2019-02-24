from django.contrib import admin

from .models import ShortURL


class ShortURLAdmin(admin.ModelAdmin):
    search_fields = ['full_url']
    list_display = ('full_url', 'code', 'create_date')

admin.site.register(ShortURL, ShortURLAdmin)
