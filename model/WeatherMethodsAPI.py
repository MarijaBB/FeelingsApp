import requests
class Weather:
    def get_location(self):
        try:
            response = requests.get("https://ipinfo.io/json")  # maybe geocoder if this does not work
            response.raise_for_status() #httperror if status >299
            data = response.json()
            location = data['loc']   
            return location
        except Exception as e:
            print(f'Error getting location:{e}')
            return 'Belgrade'

    def get_weather_icon_url(self):
        API_KEY = 11111 # hidden info
        url = "http://api.weatherapi.com/v1/current.json"

        location = self.get_location()
        try:
            params = {
                "key": API_KEY,
                "q": location
            }
            response = requests.get(url, params=params)

            data = response.json()
            icon_url = 'http:' + data['current']['condition']['icon'] # on this link there is only one small picture
            return icon_url
        except KeyError:
            print('Missing icon')
        except requests.RequestException as e:
            print(f"Request to weather API failed: {e}")
        except Exception as e:
            print(f"Error retrieving weather icon URL: {e}")
        return None