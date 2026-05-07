from django.contrib import admin
from .models import Lesson

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_filter = ('status',)

admin.site.register(Lesson, LessonAdmin)
