from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField()
    birth_date  = models.DateField()
    bio = models.TextField()

class AuthorDetails(models.Model):
    email = models.EmailField()
    phone = models.CharField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

class Publisher (models.Model):
    name = models.CharField()
    address  = models.TextField()

class Genre(models.Model):
    name = models.CharField()

class Book(models.Model):
    title = models.CharField()
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher  = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
