from django.db import models

# Create your models here.

class Manager(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)

