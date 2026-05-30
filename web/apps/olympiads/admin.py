from django.contrib import admin
from .models import Olympiad, OlympiadTask, OlympiadTaskAnswer

class OlympiadTaskInline(admin.TabularInline):
    model = OlympiadTask
    extra = 1

class OlympiadTaskAnswerInline(admin.TabularInline):
    model = OlympiadTaskAnswer
    extra = 1

@admin.register(Olympiad)
class OlympiadAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "subject", "date")
    list_filter = ("subject",)
    inlines = [OlympiadTaskInline]

@admin.register(OlympiadTask)
class OlympiadTaskAdmin(admin.ModelAdmin):
    list_display = ("id", "olympiad", "text")
    inlines = [OlympiadTaskAnswerInline]

@admin.register(OlympiadTaskAnswer)
class OlympiadTaskAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "task", "answer_text", "is_true")
    list_filter = ("is_true",)
