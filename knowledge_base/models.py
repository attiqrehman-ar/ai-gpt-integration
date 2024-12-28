from django.db import models

class KnowledgeBaseDocument(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='knowledge_base/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
