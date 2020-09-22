from django.apps import AppConfig
import os
import requests
import json


class WeatherConfig(AppConfig):
    name = 'weather'


    def get_weather(self, city='Gardena'):
        weather_url = 'https://api.openweathermap.org/data/2.5/weather?'
        return requests.get(weather_url + 'q=' + city + '&appid=' + os.environ.get('OPEN_WEATHER_KEY') + '&units=' + 'imperial').json()
