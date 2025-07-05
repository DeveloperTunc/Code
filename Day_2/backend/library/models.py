from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=75)
    author = models.CharField(max_length=50)
    year = models.DateField()
        
    def __str__(self):
        return f"Name:{self.name} Author:{self.author}"