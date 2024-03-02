# mylibrary/urls.py
from django.urls import path
from .views import home, book_detail , authors , book_details

urlpatterns = [
    path('', home, name='home'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('authors/', authors, name='authors'),
    path('book/<int:book_id>/', book_details, name='book_details'),
]
