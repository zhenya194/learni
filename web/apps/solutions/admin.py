from django.contrib import admin
from .models import Solution

class SolutionAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_filter = ('status',)

admin.site.register(Solution, SolutionAdmin)
