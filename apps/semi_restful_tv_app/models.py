from django.db import models

# from __future__ import unicode_literals
# from django.db import models

# class ShowManager(models.Manager):
#     def basic_validator(self, postData):
#         errors = {}
#         if len(postData['name'])

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField(default="Heyyyy")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)