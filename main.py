from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import jokes, images , text, weather

app = FastAPI(
    title="Multi-Service API",
    description="A portfolio project showcasing various API endpoints",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(jokes.router)
app.include_router(images.router)
app.include_router(text.router)
app.include_router(weather.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Multi-Service API",
        "documentation": "/docs",
        "version": "0.1.0"
    }