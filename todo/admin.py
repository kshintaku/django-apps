from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Task", {"fields": ["title", "complete", "paused"]}),
        ("Date information", {"fields": ["date"]}),
    ]
    list_display = ("title", "complete", "date")


admin.site.register(Todo, TodoAdmin)
