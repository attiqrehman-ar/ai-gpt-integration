from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import KnowledgeBaseDocument
from PyPDF2 import PdfReader  # For extracting text from PDF
import openai  # OpenAI LLM integration

# Function to extract text from PDFs (could add more types of file extraction here)
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Document Upload View
def upload_document(request):
    if request.method == 'POST' and request.FILES['document']:
        uploaded_file = request.FILES['document']
        title = request.POST.get('title', '')
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)

        # Extract content (Assuming PDF for simplicity)
        content = ""
        if uploaded_file.name.endswith('.pdf'):
            content = extract_text_from_pdf(uploaded_file)
        else:
            content = uploaded_file.read().decode('utf-8')  # For text files

        # Save document to database
        document = KnowledgeBaseDocument(title=title, file=file_url, content=content)
        document.save()

        return redirect('knowledge_base:document_list')

    return render(request, 'knowledge_base/upload_document.html')

# List all documents
def document_list(request):
    documents = KnowledgeBaseDocument.objects.all()
    return render(request, 'knowledge_base/document_list.html', {'documents': documents})

# AI Agent Chat View
def ai_chat(request):
    query = request.GET.get('query', '')
    response = ""

    if query:
        # Check if the query matches any documents in the knowledge base
        document = KnowledgeBaseDocument.objects.filter(content__icontains=query).first()
        if document:
            response = f"Found answer in document: {document.title}. Content: {document.content[:500]}..."  # Return a snippet
        else:
            # Fall back to LLM if no document matches
            response = query_with_llm(query)

    return render(request, 'chat/chat_home.html', {'response': response, 'query': query})

# Function to interact with LLM (e.g., OpenAI GPT-3)
def query_with_llm(query):
    openai.api_key = 'your-openai-api-key'  # Replace with your OpenAI API key

    # Query OpenAI's model for the response
    response = openai.Completion.create(
        model="text-davinci-003",  # Or use a different model as needed
        prompt=query,
        max_tokens=150
    )

    return response.choices[0].text.strip()
