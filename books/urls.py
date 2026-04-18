from django.urls import path
from .views import books_api, ask_ai, home

urlpatterns = [
    path('', home),
    path('books/', books_api),   
    path('ask/', ask_ai),
]