from django.db import models
from django.conf import settings
from api.models import Book


class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Cart {self.id}"


class CartItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(
        Cart, related_name="items", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.quantity} of {self.book.title}"
