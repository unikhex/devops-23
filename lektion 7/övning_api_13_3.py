import requests

# Funktion för att hämta väderrapporter för en stad från API:et
def get_weather(city):
    api_url = f'https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/{city.lower()}'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Funktion för att skriva ut väderrapporter
def print_weather(city, weather_data):
    if weather_data:
        print(f"Väderrapporter för {city.capitalize()} de kommande fem dagarna:")
        for day, report in enumerate(weather_data['forecasts'], start=1):
            print(f"Dag {day}: {report}")
    else:
        print(f"Kunde inte hämta väderrapporter för {city.capitalize()}.")

# Huvudprogram
try:
    user_city = input("Ange en stad (Stockholm, Göteborg, Malmö, Uppsala, Västerås): ").strip().lower()
    if user_city in ["stockholm", "göteborg", "malmö", "uppsala", "västerås"]:
        weather_data = get_weather(user_city)
        print_weather(user_city, weather_data)
    else:
        print("Ogiltig stad. Ange en av de tillgängliga städerna.")
except ValueError:
    print("Felaktig inmatning.")
