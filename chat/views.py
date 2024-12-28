from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .openai_utils import ask_openai


def ask_ai_page(request):
    return render(request, 'chat/chat_home.html')
@csrf_exempt
def ask_question(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            question = data.get("question", "")
            if not question:
                return JsonResponse({"error": "Question not provided"}, status=400)

            response = ask_openai(question)
            return JsonResponse({"answer": response}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


import openai

def ask_openai(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ]
        )
        return response['choices'][0]['message']['content']
    except openai.error.RateLimitError:
        return "It seems you've exceeded your quota. Please check your usage or consider other options."
    except openai.error.OpenAIError as e:
        return f"An error occurred: {str(e)}"
