# 🧠 Multi-Service API Portfolio Project

This project is a Python-based REST API built with FastAPI, designed to showcase various integrations and functionalities, including interactions with OpenAI, Unsplash, and WeatherAPI. It serves as a demonstration of building scalable and modular APIs, suitable for inclusion in a professional GitHub portfolio.

## 🚀 Project Overview

The Multi-Service API offers a range of endpoints:

- **Joke Generator**: Produces random or topic-specific jokes using OpenAI
- **Image Fetcher**: Retrieves daily or category-based images from Unsplash
- **Text Processor**: Provides text summarization, translation, and sentiment analysis via OpenAI
- **Weather Information**: Delivers current weather data and forecasts using WeatherAPI

Each endpoint is designed to be modular, easily testable, and well-documented through FastAPI's interactive Swagger UI.

## 🧰 Tech Stack

- **Backend Framework**: FastAPI
- **Language**: Python 3.10
- **Asynchronous HTTP Client**: httpx
- **Environment Management**: python-dotenv
- **Containerization**: Docker
- **API Integrations**:
  - OpenAI API
  - Unsplash API
  - WeatherAPI

## 🧠 Skills Demonstrated

- **API Development**: Designed RESTful APIs with FastAPI, including routing, middleware, and dependency injection
- **Third-Party Integration**: Integrated external APIs (OpenAI, Unsplash, WeatherAPI) securely and efficiently
- **Asynchronous Programming**: Utilized async/await syntax for non-blocking I/O operations
- **Environment Configuration**: Managed sensitive information using environment variables and .env files
- **Containerization**: Dockerized the application for consistent deployment across environments
- **Documentation**: Leveraged FastAPI's automatic documentation generation for clear API specs

## 📁 Project Structure

```
project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── jokes.py
│   │   ├── images.py
│   │   ├── text.py
│   │   └── weather.py
│   └── utils/
│       ├── __init__.py
│       └── openai_helper.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── Dockerfile
└── README.md
```

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/noorullah1102/fastapi-portfolio-project
cd fastapi-portfolio-project
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```bash
OPENAI_API_KEY=your_openai_api_key
WEATHER_API_KEY=your_weatherapi_key
UNSPLASH_API_KEY=your_unsplash_api_key
```

Ensure `.env` is listed in `.gitignore` to prevent committing sensitive information.

### 5. Run the Application

```bash
uvicorn app.main:app --reload
```

Access the API at `http://localhost:8000` and the interactive documentation at `http://localhost:8000/docs`.

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t multi-service-api .
```

### Run Docker Container

```bash
docker run -p 8000:8000 --env-file .env multi-service-api
```

Access the API at `http://localhost:8000` and the interactive documentation at `http://localhost:8000/docs`.

## 📚 API Endpoints

### Root

**GET** `/`

Description: Provides a welcome message and basic API information.

Response:
```json
{
  "message": "Welcome to Multi-Service API",
  "documentation": "/docs",
  "version": "0.1.0"
}
```

### Jokes

**GET** `/jokes/random`

Description: Generates a random joke.

Query Parameters:
- `type` (optional): Type of joke (general, dad, pun, knock-knock)

Response:
```json
{
  "joke": "Why don't scientists trust atoms? Because they make up everything!",
  "type": "general"
}
```

**GET** `/jokes/custom`

Description: Generates a joke based on a specific topic and type.

Query Parameters:
- `topic` (required): Topic for the joke
- `type` (optional): Type of joke

Response:
```json
{
  "joke": "Why did the developer go broke? Because he used up all his cache.",
  "type": "pun",
  "topic": "developer"
}
```

### Images

**GET** `/images/daily`

Description: Fetches the image of the day from Unsplash.

Response:
```json
{
  "image_url": "https://images.unsplash.com/photo-...",
  "photographer": "Jane Doe",
  "description": "A beautiful sunrise over the mountains.",
  "download_url": "https://unsplash.com/photos/..."
}
```

**GET** `/images/category/{category}`

Description: Fetches a random image from a specified category.

Path Parameters:
- `category`: Category of the image (e.g., nature, technology)

Response:
```json
{
  "category": "nature",
  "image_url": "https://images.unsplash.com/photo-...",
  "photographer": "John Smith",
  "description": "Lush green forest during daytime."
}
```

### Text Processing

**POST** `/text/summarize`

Description: Summarizes the provided text.

Request Body:
```json
{
  "text": "Artificial Intelligence (AI) is a branch of computer science..."
}
```

Query Parameters:
- `length` (optional): Desired summary length (short, medium, long)

Response:
```json
{
  "summary": "AI is a computer science field focused on creating intelligent machines.",
  "original_length": 123
}
```

**POST** `/text/translate`

Description: Translates the provided text into the target language.

Request Body:
```json
{
  "text": "Hello, how are you?"
}
```

Query Parameters:
- `target_language` (required): Language to translate the text into (e.g., Spanish)

Response:
```json
{
  "translation": "Hola, ¿cómo estás?",
  "language": "Spanish"
}
```

**POST** `/text/sentiment`

Description: Analyzes the sentiment of the provided text.

Request Body:
```json
{
  "text": "I am thrilled with the new features!"
}
```

Response:
```json
{
  "sentiment": "positive",
  "text": "I am thrilled with the new features!"
}
```

### Weather

**GET** `/weather/current`

Description: Retrieves current weather information for a specified city.

Query Parameters:
- `city` (required): Name of the city

Response:
```json
{
  "location": "Kuala Lumpur, Malaysia",
  "temperature_c": 30.5,
  "temperature_f": 86.9,
  "condition": "Partly cloudy",
  "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
  "humidity": 70,
  "wind_kph": 15.0,
  "updated": "2025-05-23 16:00"
}
```

**GET** `/weather/forecast`

Description: Retrieves weather forecast for a specified city.

Query Parameters:
- `city` (required): Name of the city
- `days` (optional): Number of days for forecast (1-7, default: 3)

Response:
```json
{
  "location": "Kuala Lumpur, Malaysia",
  "forecast": [
    {
      "date": "2025-05-23",
      "max_temp_c": 32.0,
      "min_temp_c": 24.0,
      "condition": "Partly cloudy",
      "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
      "chance_of_rain": "20%"
    }
  ]
}
```

## 🔧 Dependencies

```
fastapi==0.104.1
uvicorn==0.23.2
python-dotenv==1.0.0
openai==1.3.0
httpx==0.25.1
python-multipart==0.0.6
pydantic==2.4.2
```

## 🚀 Getting Started for Development

1. **API Keys Setup**: You'll need to obtain API keys from:
   - [OpenAI](https://platform.openai.com/api-keys)
   - [Unsplash](https://unsplash.com/developers)
   - [WeatherAPI](https://weatherapi.com/)

2. **Environment Variables**: Copy `.env.example` to `.env` and fill in your API keys

3. **Testing**: Visit `http://localhost:8000/docs` to interact with the API using FastAPI's built-in Swagger UI

