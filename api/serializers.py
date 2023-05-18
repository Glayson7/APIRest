from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "description",
            "image",
            "price",
            "rating",
        ]  # Atualize esta lista com os novos campos
