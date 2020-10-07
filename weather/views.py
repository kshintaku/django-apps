# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import os

# import json

from .forms import SearchLocForm
from .forms import UnitToggleForm

# Create your views here.
loc_obj = {}
weather_obj = {}
weather_plus_obj = {}
error_obj = {}
main_display = {}


def spec_city(request, city):
    form = SearchLocForm()
    call_weather(city)
    template = loader.get_template("weather/index.html")
    context = {
        "error": error_obj,
        "location": loc_obj,
        "main_display": main_display,
        "weather": weather_obj,
        "form": form,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    unit = UnitToggleForm()
    if request.method == "POST":
        form = SearchLocForm(request.POST)
        if form.is_valid():
            call_weather(form.cleaned_data["loc_info"])
            form = SearchLocForm()
    else:
        form = SearchLocForm()
    template = loader.get_template("weather/index.html")
    context = {
        "error": error_obj,
        "location": loc_obj,
        "main_display": main_display,
        "weather": weather_obj,
        "form": form,
        "unit": unit,
        "weather_plus": weather_plus_obj,
    }
    return HttpResponse(template.render(context, request))


def call_weather(city):
    weather_data = get_weather(city)
    if weather_data["cod"] != 200:
        error_obj["code"] = weather_data["cod"]
        error_obj["message"] = weather_data["message"]
        loc_obj["city"] = ""
        weather_obj["humidity"] = ""
        main_display["main"] = ""
    else:
        loc_obj["city"] = weather_data["name"]
        loc_obj["latitude"] = weather_data["coord"]["lat"]
        loc_obj["longitude"] = weather_data["coord"]["lon"]
        loc_obj["timezone offset"] = weather_data["timezone"]

        main_display["temperature"] = "{:.1f}°".format(weather_data["main"]["temp"])
        weather_obj["min temperature"] = "{:.1f}°".format(
            weather_data["main"]["temp_min"]
        )
        weather_obj["max temperature"] = "{:.1f}°".format(
            weather_data["main"]["temp_max"]
        )
        weather_obj["humidity"] = "{}%".format(weather_data["main"]["humidity"])
        weather_obj["wind speed"] = "{:.1f}".format(weather_data["wind"]["speed"])
        main_display["description"] = weather_data["weather"][0]["description"]
        main_display["main"] = weather_data["weather"][0]["main"]
        main_display["icon"] = "http://openweathermap.org/img/wn/{}@2x.png".format(
            weather_data["weather"][0]["icon"]
        )
        more_weather_data = get_weather_plus(loc_obj["latitude"], loc_obj["longitude"])
        for idx, val in enumerate(more_weather_data["daily"]):
            dict_key = "day" + str(idx + 1)
            weather_plus_obj[dict_key] = ["{:.1f}°".format(val["temp"]["day"]), "{:.1f}°".format(val["temp"]["min"]), "{:.1f}°".format(val["temp"]["max"])]


def get_weather(city):
    weather_url = "https://api.openweathermap.org/data/2.5/weather?"
    return requests.get(
        weather_url
        + "q="
        + city
        + "&appid="
        + os.environ.get("OPEN_WEATHER_KEY")
        + "&units="
        + "imperial"
    ).json()

def get_weather_plus(lat, lon):
    weather_url = "https://api.openweathermap.org/data/2.5/onecall?"
    return requests.get(
        weather_url
        + "lat="
        + str(loc_obj["latitude"])
        + "&lon="
        + str(loc_obj["longitude"])
        + "&exclude=current,minutely,hourly"
        + "&appid="
        + os.environ.get("OPEN_WEATHER_KEY")
        + "&units="
        + "imperial"
    ).json()
