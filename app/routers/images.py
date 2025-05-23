import os
import httpx
from fastapi import APIRouter, Query, HTTPException
from dotenv import load_dotenv

load_dotenv()
router = APIRouter(prefix="/images", tags=["images"])

UNSPLASH_API_KEY = os.getenv("UNSPLASH_API_KEY")

@router.get("/daily")
async def get_image_of_day():
    """Fetch the image of the day from Unsplash"""
    if not UNSPLASH_API_KEY:
        raise HTTPException(status_code=500, detail="Unsplash API key not configured")
    
    url = "https://api.unsplash.com/photos/random"
    headers = {"Authorization": f"Client-ID {UNSPLASH_API_KEY}"}
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch image")
        
        data = response.json()
        return {
            "image_url": data["urls"]["regular"],
            "photographer": data["user"]["name"],
            "description": data.get("description") or data.get("alt_description") or "No description available",
            "download_url": data["links"]["download"]
        }

@router.get("/category/{category}")
async def get_image_by_category(category: str):
    """Fetch a random image from a specific category"""
    if not UNSPLASH_API_KEY:
        raise HTTPException(status_code=500, detail="Unsplash API key not configured")
    
    url = f"https://api.unsplash.com/photos/random?query={category}"
    headers = {"Authorization": f"Client-ID {UNSPLASH_API_KEY}"}
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch image")
        
        data = response.json()
        return {
            "category": category,
            "image_url": data["urls"]["regular"],
            "photographer": data["user"]["name"],
            "description": data.get("description") or data.get("alt_description") or "No description available"
        }
