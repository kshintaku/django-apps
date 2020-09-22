from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
from .apps import WeatherConfig

# Create your views here.
loc_obj = {}
weather_obj = {}

def index(request):
  call_weather()
  template = loader.get_template('weather/index.html')
  context = {
    'location': loc_obj,
    'weather': weather_obj,
  }
  return HttpResponse(template.render(context, request))

def call_weather(city='Torrance'):
  weather_data = WeatherConfig.get_weather(city)
  loc_obj['city'] = weather_data['name']
  loc_obj['lat'] = weather_data['coord']['lat']
  loc_obj['long'] = weather_data['coord']['lon']
  loc_obj['timezone_offset'] = weather_data['timezone']

  weather_obj['temp'] = weather_data['main']['temp']
  weather_obj['temp_min'] = weather_data['main']['temp_min']
  weather_obj['temp_max'] = weather_data['main']['temp_max']
  weather_obj['humidity'] = weather_data['main']['humidity']
  weather_obj['wind_spd'] = weather_data['wind']['speed']