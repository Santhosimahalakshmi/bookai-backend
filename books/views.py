from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

# Temporary in-memory storage (you can replace with DB later)
books = []

# ------------------------
# ADD + GET BOOKS API
# ------------------------
@csrf_exempt
def books_api(request):
    if request.method == "GET":
        return JsonResponse(books, safe=False)

    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title")
        author = data.get("author")

        if not title or not author:
            return JsonResponse({"error": "Missing fields"}, status=400)

        book = {
            "title": title,
            "author": author
        }

        books.append(book)

        return JsonResponse({"message": "Book added successfully"})

# ------------------------
# ASK AI (LM STUDIO)
# ------------------------
@csrf_exempt
def ask_ai(request):
    if request.method == "POST":
        data = json.loads(request.body)
        question = data.get("question")

        if not question:
            return JsonResponse({"error": "Question missing"}, status=400)

        try:
            response = requests.post(
                "http://localhost:1234/v1/chat/completions",
                json={
                    "model": "local-model",
                    "messages": [
                        {"role": "user", "content": question}
                    ]
                }
            )

            result = response.json()

            # Extract answer safely
            answer = result.get("choices", [{}])[0].get("message", {}).get("content", "No response")

            return JsonResponse({"answer": answer})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Backend is running 🚀"})