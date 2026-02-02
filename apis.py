import requests

def get_weather(city, api_key, units='imperial'):
    """
    Fetches current weather for a city.
    Units: 'metric' (Celsius), 'imperial' (Fahrenheit), or 'standard' (Kelvin).
    """
    URL = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API call
    params = {
        'q': city,
        'appid': api_key,
        'units': units
    }

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()

        # Extract specific data points
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']
        country = data['sys']['country']

        # Determine unit labels
        temp_unit = "°C" if units == 'metric' else "°F" if units == 'imperial' else "K"
        wind_unit = "m/s" if units != 'imperial' else "mph"

        print(f"--- Current Weather in {city.title()} ---")
        print(f"Location: {country}")
        print(f"Condition: {description.capitalize()}")
        print(f"Temperature: {temp}{temp_unit}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} {wind_unit}")

    except Exception as e:
        print(f"An unexpected error occurred! {e}")

if __name__ == "__main__":
    API_KEY = "88723180e3c19e3235dfaf41df75b619"
    city = input("Enter a city name: ")
    get_weather(city, API_KEY, units='imperial')
