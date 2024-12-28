from django.urls import path
from . import views
app_name = 'knowledge_base' 
urlpatterns = [
    path('upload/', views.upload_document, name='upload_document'),
    path('documents/', views.document_list, name='document_list'),  # Added route for listing documents
    path('chatt/', views.ai_chat, name='ai_chat'), 
]
