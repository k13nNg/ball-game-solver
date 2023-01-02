from django.db import models

# Create your models here.
class Ball(models.Model):
    color = models.CharField(max_length=200)
    y_pos = models.IntegerField(default=0)