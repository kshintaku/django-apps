from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import os
import requests
import json

# Create your views here.
loc_obj = {}
weather_obj = {}

def spec_city(request, city):
  call_weather(city)
  # print(city)
  template = loader.get_template('weather/index.html')
  context = {
    'location': loc_obj,
    'weather': weather_obj,
  }
  return HttpResponse(template.render(context, request))

def index(request):
  template = loader.get_template('weather/index.html')
  context = {
    'location': loc_obj,
    'weather': weather_obj,
  }
  return HttpResponse(template.render(context, request))

def call_weather(city):
  print(city)
  weather_data = get_weather(city)
  # weather_data = WeatherConfig.get_weather(cityy)
  loc_obj['city'] = weather_data['name']
  print(loc_obj['city'])
  loc_obj['latitude'] = weather_data['coord']['lat']
  loc_obj['longitude'] = weather_data['coord']['lon']
  loc_obj['timezone offset'] = weather_data['timezone']

  weather_obj['temperature'] = weather_data['main']['temp']
  weather_obj['min temperature'] = weather_data['main']['temp_min']
  weather_obj['max temperature'] = weather_data['main']['temp_max']
  weather_obj['humidity'] = weather_data['main']['humidity']
  weather_obj['wind speed'] = weather_data['wind']['speed']

def get_weather(city):
  print(city)
  weather_url = 'https://api.openweathermap.org/data/2.5/weather?'
  return requests.get(weather_url + 'q=' + city + '&appid=' + os.environ.get('OPEN_WEATHER_KEY') + '&units=' + 'imperial').json()
