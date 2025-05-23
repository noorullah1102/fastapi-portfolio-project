from fastapi import APIRouter, Body, Query
from app.utils.openai_helper import generate_completion
from pydantic import BaseModel

router = APIRouter(prefix="/text", tags=["text"])

class TextInput(BaseModel):
    text: str

@router.post("/summarize")
async def summarize_text(
    input_data: TextInput,
    length: str = Query("short", description="Length of summary: short, medium, long")
):
    """Summarize the provided text using OpenAI"""
    prompt = f"Summarize the following text in a {length} summary:\n\n{input_data.text}"
    summary = generate_completion(prompt, max_tokens=300)
    return {"summary": summary, "original_length": len(input_data.text)}

@router.post("/translate")
async def translate_text(
    input_data: TextInput,
    target_language: str = Query(..., description="Target language for translation")
):
    """Translate the provided text to the target language"""
    prompt = f"Translate the following text to {target_language}:\n\n{input_data.text}"
    translation = generate_completion(prompt, max_tokens=300)
    return {"translation": translation, "language": target_language}

@router.post("/sentiment")
async def analyze_sentiment(input_data: TextInput):
    """Analyze the sentiment of the provided text"""
    prompt = f"Analyze the sentiment of the following text. Return only one word: 'positive', 'negative', or 'neutral'.\n\n{input_data.text}"
    sentiment = generate_completion(prompt, max_tokens=10).strip().lower()
    
    # Ensure the sentiment is one of the expected values
    valid_sentiments = ["positive", "negative", "neutral"]
    if sentiment not in valid_sentiments:
        sentiment = "neutral"  # Default if unexpected response
    
    return {"sentiment": sentiment, "text": input_data.text}
