from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Rows(models.Model):
    id = models.AutoField(primary_key=True)
    new_hire_id = models.CharField(max_length=30)
    new_hire_name = models.CharField(max_length=30)
    manager_id = models.CharField(max_length=30)
    manager_name = models.CharField(max_length=30)
