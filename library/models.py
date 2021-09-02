from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name

    # def clean(self):
    #     if self.name[0].isdigit():
    #         raise ValidationError("Author Name cannot start with a digit")

class Book(models.Model):
    name = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"

    def __str__(self):
        return self.name
