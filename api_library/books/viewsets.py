from rest_framework import viewsets
from books.serializer import BookSerializer
from books.models import Books

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Books.objects.all()