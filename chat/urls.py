from django.urls import path
from .views import ask_question, chat_home

urlpatterns = [
    path('', chat_home, name='chat_home'),  # Render the AI chat interface
    path('ask/', ask_question, name='ask_question'),  # Handle AI API requests
]
