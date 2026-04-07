import requests
from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render

def home(request):
    city = request.GET.get("city", "Athens")
    cache_key = f"weather_{city.lower()}"
    cached = cache.get(cache_key)

    if cached:
        cached["cached"] = True
        return render(request, "weather/home.html", cached)

    api_key = settings.WEATHER_API_KEY

    url = (
        f"http://api.weatherapi.com/v1/forecast.json?"
        f"key={api_key}&q={city}&days=3&aqi=no&alerts=no"
    )

    data = requests.get(url).json()

    if "error" in data:
        return render(request, "weather/home.html", {"error": data["error"]["message"]})

    location = data["location"]
    current = data["current"]
    forecast_days = data["forecast"]["forecastday"]

    context = {
        "city": location["name"],
        "country": location["country"],
        "temperature": current["temp_c"],
        "humidity": current["humidity"],
        "wind": current["wind_kph"],
        "pressure": current["pressure_mb"],
        "description": current["condition"]["text"],
        "icon": "https:" + current["condition"]["icon"],
        "forecast": [
            {
                "date": day["date"],
                "max": day["day"]["maxtemp_c"],
                "min": day["day"]["mintemp_c"],
                "text": day["day"]["condition"]["text"],
                "icon": "https:" + day["day"]["condition"]["icon"],
            }
            for day in forecast_days
        ],
        "cached": False,
    }

    cache.set(cache_key, context, timeout=600)
    return render(request, "weather/home.html", context)
