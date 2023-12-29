import requests
import json

# Fetch weather data
def fetch_weather(api_key, latitude, longitude):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

# Get current location and coordinates
def get_current_location():
    # Implement your logic to get the user's location or use geocoding libraries
    latitude = 0.0  # Replace with the actual latitude
    longitude = 0.0  # Replace with the actual longitude
    return latitude, longitude

# Main program
def rain():
    api_key = "5549adb13e3815dd78cdec57835b881c"  # Replace with your OpenWeatherMap API key

    latitude, longitude = get_current_location()
    weather_data = fetch_weather(api_key, latitude, longitude)

    # Extract relevant information
    temperature = weather_data["main"]["temp"]
    rainfall_prediction = weather_data["rain"]["1h"] if "rain" in weather_data else "N/A"

    # Display information
    print(f"Current temperature: {temperature}°C")
    print(f"Rainfall prediction: {rainfall_prediction} mm")

if __name__ == "__rain__":
    rain()
