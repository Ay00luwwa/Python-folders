import requests
import json

API_KEY = "de46fcb2772c80be26891eaa727e7aca"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def main():
    city = input("Enter the name of the city: ")
    weather_data = get_weather(city)
    if weather_data["cod"] == "404":
        print("City not found!")
    else:
        try:
            temperature = weather_data["main"]["temp"]
            weather_description = weather_data["weather"][0]["description"]
            print(f"The temperature in {city} is {temperature}°C.")
            print(f"The weather is {weather_description}.")
        except KeyError as e:
            print("Error: Invalid API response format.")
            print(f"KeyError: {e}")


