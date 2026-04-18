from django.urls import path
from .views import books_api, ask_ai

urlpatterns = [
    path('books/', books_api),
    path('ask/', ask_ai),
]