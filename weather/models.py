from django.db import models


class LocationManager(models.Manager):
    def create_location(self, city, lat, lon, tz, tzo):
        loc = self.create(
            city=city, latitude=lat, longitude=lon, timezone=tz, timezone_offset=tzo
        )
        return loc


class Location(models.Model):
    city = models.CharField("City", max_length=100)
    latitude = models.FloatField("Latitude")
    longitude = models.FloatField("Longitude")
    timezone = models.CharField("Time Zone", max_length=100)
    timezone_offset = models.IntegerField("timezone offset from UTC in sec")
    objects = LocationManager()


class WeatherManager(models.Manager):
    def create_weather(self, time, temp, uv, ws):
        weather = self.create(
            weather_time=time, current_temp=temp, current_uv=uv, current_wind_speed=ws
        )
        return weather


class Weather(models.Model):
    weather_time = models.DateTimeField("Current Time")
    current_temp = models.FloatField("Current Temp")
    current_uv = models.FloatField("UV Index", blank=True)
    current_wind_speed = models.FloatField("Wind Speed")
    objects = WeatherManager()
