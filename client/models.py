from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.client_name