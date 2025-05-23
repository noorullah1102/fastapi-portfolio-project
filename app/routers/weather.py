import os
import httpx
from fastapi import APIRouter, Query, HTTPException
from dotenv import load_dotenv

load_dotenv()
router = APIRouter(prefix="/weather", tags=["weather"])

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

@router.get("/current")
async def get_current_weather(city: str = Query(..., description="City name")):
    """Get current weather for a specific city"""
    if not WEATHER_API_KEY:
        raise HTTPException(status_code=500, detail="Weather API key not configured")
    
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=no"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch weather data")
        
        data = response.json()
        
        return {
            "location": f"{data['location']['name']}, {data['location']['country']}",
            "temperature_c": data['current']['temp_c'],
            "temperature_f": data['current']['temp_f'],
            "condition": data['current']['condition']['text'],
            "icon": data['current']['condition']['icon'],
            "humidity": data['current']['humidity'],
            "wind_kph": data['current']['wind_kph'],
            "updated": data['current']['last_updated']
        }

@router.get("/forecast")
async def get_weather_forecast(
    city: str = Query(..., description="City name"),
    days: int = Query(3, description="Number of days for forecast (1-7)")
):
    """Get weather forecast for a specific city"""
    if not WEATHER_API_KEY:
        raise HTTPException(status_code=500, detail="Weather API key not configured")
    
    if not 1 <= days <= 7:
        raise HTTPException(status_code=400, detail="Days parameter must be between 1 and 7")
    
    url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={city}&days={days}&aqi=no"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch forecast data")
        
        data = response.json()
        forecast_days = []
        
        for day in data['forecast']['forecastday']:
            forecast_days.append({
                "date": day['date'],
                "max_temp_c": day['day']['maxtemp_c'],
                "min_temp_c": day['day']['mintemp_c'],
                "condition": day['day']['condition']['text'],
                "icon": day['day']['condition']['icon'],
                "chance_of_rain": f"{day['day']['daily_chance_of_rain']}%"
            })
        
        return {
            "location": f"{data['location']['name']}, {data['location']['country']}",
            "forecast": forecast_days
        }