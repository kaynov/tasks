from django.contrib import admin
from .models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "status",
        "start",
        "end",
    )
    readonly_fields = ["start", "end"]
    list_filter = ["status"]
    search_fields = ("name",)
