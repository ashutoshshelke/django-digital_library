from random import choices
from turtle import title
from unicodedata import decimal
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Author(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHERS = 'O'
    
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHERS, 'Others'),
    ]

    name = models.CharField(max_length=255)
    pen_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.CharField(max_length=3)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.name + f" ({self.pen_name})"

class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField(null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)