import requests
import json

url = 'https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/stockholm'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request was not successful
    response_dictionary = json.loads(response.text)
    print(response_dictionary)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
except json.JSONDecodeError as e:
    print("JSON decoding error:", e)
