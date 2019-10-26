from django.contrib import admin

from .models import Character, Stats

# Register your models here.
class StatsInline(admin.TabularInline):
    model = Stats
    verbose_name_plural = "Stats"
    extra = 1

class CharacterAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['char_name', 'char_origin', 'char_img']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    inlines = [
        StatsInline,
    ]

    list_filter = ['pub_date']

    search_fields = ['char_name']

    list_display = ('char_name', 'char_origin', 'pub_date')

admin.site.register(Character, CharacterAdmin)
