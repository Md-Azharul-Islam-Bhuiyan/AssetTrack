from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=30)
    slug=models.SlugField(max_length=30) 

    def __str__(self):
        return self.name
