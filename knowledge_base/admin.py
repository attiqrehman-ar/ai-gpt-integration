from django.contrib import admin
from .models import KnowledgeBaseDocument

class KnowledgeBaseDocumentAdmin(admin.ModelAdmin):
    # List display for the KnowledgeBaseDocument admin interface
    list_display = ('title', 'document', 'uploaded_at')  # Adjust this as per your model

    def document(self, obj):
        return obj.file.name  # If you have a file field called 'file'

    # Optionally, if you have custom methods, add them to list_display

admin.site.register(KnowledgeBaseDocument, KnowledgeBaseDocumentAdmin)
