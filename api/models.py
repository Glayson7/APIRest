from django.db import models
from django.db.models import Q


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="book_images/", null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True
    )
    stock = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category)  # New field for categories

    def __str__(self):
        return self.title

    @staticmethod
    def search(query):
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
