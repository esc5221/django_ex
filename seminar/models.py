from django.db import models

# Create your models here.
class Seminar(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
