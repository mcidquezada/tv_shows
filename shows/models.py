# Create your models here.
from enum import auto
from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # if len(data['title']) < 2:
        #     errors['title'] = 'Show title must be at least 2 characters'
        # if len(data['network']) < 3:
        #     errors['network'] = 'Network must be at least 3 characters'
        # if len(data['description']) < 5 and len(data['description']) != 0:
        #     errors['description'] = 'Show description must be at least 10 characters'
        return errors


class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_At =models.DateTimeField(auto_now_add=True)
    objects = ShowManager()

