from django.contrib.auth import get_user_model
from django.db import models
from api.models import Book

User = get_user_model()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user.username} review for {self.book.title}'

    class Meta:
        unique_together = [['user', 'book']]
