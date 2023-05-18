from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def search(request):
    query = request.GET.get('q', '')
    books = Book.search(query)
    return JsonResponse({'books': list(books.values())})
