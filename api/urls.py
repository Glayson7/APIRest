from django.urls import path
from .views import BookList, BookDetail
from . import views

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('search/', views.search, name='search'),
]
