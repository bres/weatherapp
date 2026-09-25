# Django Weather App 🌦️

A clean, high-performance web application built with **Django** that provides real-time weather data and multi-day forecasts for any city using the WeatherAPI. Designed with built-in caching to optimize API usage and enhance user experience.

---

## 🚀 Features

* **Current Weather Conditions:** Real-time temperature, humidity, wind speed, atmospheric pressure, and weather descriptions.
* **3-Day Forecast:** Detailed daily forecasts including maximum/minimum temperatures and condition icons.
* **Performance Caching:** Utilizes Django's caching framework to store weather data for 10 minutes per city, reducing external API calls and improving load times.
* **Smart Search:** Easily query weather details for different locations dynamically via URL parameters.
* **Error Handling:** Gracefully handles invalid city queries or API connectivity issues.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **API Integration:** WeatherAPI (`requests`)
* **Caching:** Django Cache Backend
* **Frontend:** HTML5, CSS / Tailwind (rendered via Django Templates)

---

## ⚙️ Getting Started

Follow these steps to set up and run the project locally on your machine.

### Prerequisites

* Python 3.8 or higher
* pip (Python package manager)
* A free API key from [WeatherAPI](https://www.weatherapi.com/)

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/django-weather-app.git
   cd django-weather-app
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django requests
   ```

4. **Configure your API Key:**
   Make sure your Django settings (`settings.py`) include your WeatherAPI key:
   ```python
   WEATHER_API_KEY = "your_actual_api_key_here"
   ```

5. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser:**
   Navigate to `http://127.0.0.1:8000/` to use the application!

---
