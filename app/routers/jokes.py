from fastapi import APIRouter, Query
from app.utils.openai_helper import generate_completion

router = APIRouter(prefix="/jokes", tags=["jokes"])

@router.get("/random")
async def get_random_joke(
    type: str = Query("general", description="Type of joke: general, dad, pun, knock-knock")
):
    """Generate a random joke using OpenAI"""
    prompt = f"Generate a short, funny {type} joke. Just return the joke with no additional text."
    joke = generate_completion(prompt, max_tokens=100)
    return {"joke": joke, "type": type}

@router.get("/custom")
async def get_custom_joke(
    topic: str = Query(None, description="Topic for the joke"),
    type: str = Query("general", description="Type of joke")
):
    """Generate a custom joke based on topic and type"""
    prompt = f"Generate a short, funny {type} joke about {topic}. Just return the joke with no additional text."
    joke = generate_completion(prompt, max_tokens=100)
    return {"joke": joke, "type": type, "topic": topic}
