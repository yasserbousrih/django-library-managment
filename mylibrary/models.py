
from django.db import models
from django.utils import timezone

class Author(models.Model):
    first_name = models.CharField(max_length=200, default='first name')
    last_name = models.CharField(max_length=200, default='last name')
    date_of_birth = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField()
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status_choices = [
        ('m', 'Maintenance'),
        ('b', 'Booked'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='maintenance')
    due_date = models.DateField()

    def __str__(self):
        return self.book.title
