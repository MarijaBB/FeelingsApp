from model.WeatherMethodsAPI import Weather
from view.WeatherIcon import WeatherIcon

class WeatherController:
    def __init__(self, root):
        self.model = Weather()
        self.view = WeatherIcon(root)
        self.update_weather_icon()

    def update_weather_icon(self):
        icon_url = self.model.get_weather_icon_url()
        self.view.display_icon(icon_url)