from django.contrib import admin
from .models import Quote

admin.site.site_header = "Quotes Application Administration"


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'category')
    search_fields = ('text', 'author', 'category')
    list_filter = ('author', 'category')
    ordering = ('author',)


admin.site.register(Quote, QuoteAdmin)
