from django.db import models
from django.core.exceptions import ValidationError





class Category(models.Model):
    name = models.CharField(max_length=100 , unique=True)

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    author = models.CharField(max_length=100)
    year = models.IntegerField(default=2000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
