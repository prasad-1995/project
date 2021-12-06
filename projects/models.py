from django.db import models
# Create your models here.
from client.models import Client


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client_name = models.ForeignKey(Client, related_name='Project_client', on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name

