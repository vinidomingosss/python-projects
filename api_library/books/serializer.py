from books.models import Books

from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'