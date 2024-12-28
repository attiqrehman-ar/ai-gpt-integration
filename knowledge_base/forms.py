from django import forms

class KnowledgeBaseDocumentForm(forms.Form):
    title = forms.CharField(max_length=255)
    document = forms.FileField()
