import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def ask_openai(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Adjust the model if needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ],
            temperature=0.7,  # Adjust creativity level
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"
