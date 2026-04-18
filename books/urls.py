from django.urls import path
from .views import get_books, add_book, ask_ai, home

urlpatterns = [
    path('', home),   
    path('books/', get_books),
    path('add/', add_book),
    path('ask/', ask_ai),
]