from django.contrib import admin
from .models import Client

# Register your models here.


class AdminClient(admin.ModelAdmin):
    list_display = ["id", "client_name", "created_at", "created_by"]


admin.site.register(Client, AdminClient)

