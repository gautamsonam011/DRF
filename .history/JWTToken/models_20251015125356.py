from django.db import models

# Create your models here.

class Book(models.Model):
    titleName = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published = models.DateField(null = True, blank = True)

    def __str__(self):
        return f"{self.title}-{self.author}"