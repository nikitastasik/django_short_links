from django.contrib import admin
from short_link.models import Urls


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_url_id', 'long_url', 'transition_date', 'transition_count')
    ordering = ('-transition_date',)


admin.site.register(Urls, UrlsAdmin)
