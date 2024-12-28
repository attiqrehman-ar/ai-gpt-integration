from django.urls import path
from .views import ask_ai_page, ask_question

urlpatterns = [
    path('cha', ask_ai_page, name='ask_ai_page'),  # Route to render the template
    path('ask/', ask_question, name='ask_question'),  # API route
]
