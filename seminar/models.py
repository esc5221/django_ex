from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Seminar(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    nullable_capacity = models.PositiveIntegerField(null=True, blank=True)
    blankable_capacity = models.PositiveIntegerField(blank=True)
    blankable_desc = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class UserSeminar(models.Model):
    user = models.ForeignKey(get_user_model(), null=False, on_delete=models.CASCADE)
    seminar = models.ForeignKey(Seminar, null=False, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
