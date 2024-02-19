from django.db import models
from auditlog.registry import auditlog
# Create your models here.

class user(models.Model):
    user=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)

    def __str__(self):
        return self.user

