from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import os
import requests
import json

from .forms import SearchLocForm

# Create your views here.
loc_obj = {}
weather_obj = {}

def spec_city(request, city):
  form = SearchLocForm()
  call_weather(city)
  template = loader.get_template('weather/index.html')
  context = {
    'location': loc_obj,
    'weather': weather_obj,
    'form': form,
  }
  return HttpResponse(template.render(context, request))

def index(request):
  if request.method == 'POST':
    form = SearchLocForm(request.POST)
    if form.is_valid():
      call_weather(form.cleaned_data['loc_info'])
  else:
    form = SearchLocForm()
  template = loader.get_template('weather/index.html')
  context = {
    'location': loc_obj,
    'weather': weather_obj,
    'form': form,
  }
  return HttpResponse(template.render(context, request))

def call_weather(city):
  weather_data = get_weather(city)
  loc_obj['city'] = weather_data['name']
  loc_obj['latitude'] = weather_data['coord']['lat']
  loc_obj['longitude'] = weather_data['coord']['lon']
  loc_obj['timezone offset'] = weather_data['timezone']

  weather_obj['temperature'] = '{:.1f}°'.format(weather_data['main']['temp'])
  weather_obj['min temperature'] = '{:.1f}°'.format(weather_data['main']['temp_min'])
  weather_obj['max temperature'] = '{:.1f}°'.format(weather_data['main']['temp_max'])
  weather_obj['humidity'] = '{}%'.format(weather_data['main']['humidity'])
  weather_obj['wind speed'] = '{:.1f}'.format(weather_data['wind']['speed'])

def get_weather(city):
  weather_url = 'https://api.openweathermap.org/data/2.5/weather?'
  return requests.get(weather_url + 'q=' + city + '&appid=' + os.environ.get('OPEN_WEATHER_KEY') + '&units=' + 'imperial').json()
