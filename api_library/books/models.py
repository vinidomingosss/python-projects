from django.db import models

# Create your models here.

def uploadImageBook(instance, filename):
    return f'{instance} - {filename}'

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=uploadImageBook, blank=True, null=True)