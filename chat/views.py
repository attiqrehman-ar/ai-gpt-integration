from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from transformers import pipeline

# Load the Hugging Face GPT-2 model once during server startup
generator = pipeline('text-generation', model='gpt2')

@csrf_exempt
def ask_question(request):
    if request.method == "POST":
        try:
            # Parse the question from the POST request body
            data = json.loads(request.body)
            question = data.get("question", "")
            if not question:
                return JsonResponse({"error": "No question provided"}, status=400)

            # Generate a response using Hugging Face
            response = generator(question, max_length=50, num_return_sequences=1)
            answer = response[0]['generated_text']

            # Return the generated answer
            return JsonResponse({"answer": answer}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

def chat_home(request):
    # Render the HTML template
    return render(request, 'chat/chat_home.html')
