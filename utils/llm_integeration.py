from transformers import pipeline

# Define the model name you want to use
model_name = "distilbert-base-cased-distilled-squad"  # You can replace this with another model if needed

# Create the pipeline for question-answering
qa_pipeline = pipeline("question-answering", model=model_name)

def get_answer_from_knowledge_base(query, document_text):
    """
    This function uses a pre-trained LLM (question-answering model) to extract an answer
    from a provided knowledge base document.
    """

    # Prepare the context for the model (the document text)
    context = document_text

    # Use the LLM pipeline for question answering
    result = qa_pipeline({
        'question': query,
        'context': context
    })

    return result['answer']
