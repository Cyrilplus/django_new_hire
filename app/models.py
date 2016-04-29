from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Rows(models.Model):
    id = models.AutoField(primary_key=True)
    new_hire_id = models.CharField(max_length=30)
    new_hire_name = models.CharField(max_length=30)
    manager_id = models.CharField(max_length=30)
    manager_name = models.CharField(max_length=30)
    onboard_time = models.DateTimeField()
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def set_value(self, attribute, value):
        if attribute == 'new_hire_id':
            self.new_hire_id = value;
        elif attribute == 'new_hire_name':
            self.new_hire_name = value
        elif attribute == 'manager_id':
            self.manager_id = value
        elif attribute == 'manager_name':
            self.manager_name = value
        elif attribute == 'onboard_time':
            self.onboard_time = value
        elif attribute == 'created_time':
            self.created_time = value
        elif attribute == 'status':
            self.status = value
