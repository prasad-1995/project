from django.contrib import admin
from .models import Project
# Register your models here.


class AdminProject(admin.ModelAdmin):
    list_display = ["project_name", "client_name"]


admin.site.register(Project, AdminProject)