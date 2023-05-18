from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book = Book.objects.create(
            title="A Test Book", author="Test Author", pub_date="2022-01-01"
        )

    def test_get_all_books(self):
        response = self.client.get(reverse("book-list"))
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book_detail(self):
        response = self.client.get(
            reverse("book-detail", kwargs={"pk": self.book.id})
        )
        book = Book.objects.get(pk=self.book.id)
        serializer = BookSerializer(book)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_new_book(self):
        data = {
            "title": "New Test Book",
            "author": "New Test Author",
            "pub_date": "2023-01-01",
        }
        response = self.client.post(reverse("book-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        data = {
            "title": "Updated Test Book",
            "author": "Updated Test Author",
            "pub_date": "2023-01-01",
        }
        response = self.client.put(
            reverse("book-detail", kwargs={"pk": self.book.id}), data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(
            reverse("book-detail", kwargs={"pk": self.book.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
