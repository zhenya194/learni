from django.contrib import admin
from .models import LetsDoItAnyway

class LetsDoItAnywayAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_filter = ('status',)

admin.site.register(LetsDoItAnyway, LetsDoItAnywayAdmin)
