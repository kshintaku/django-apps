from django.http import HttpResponse
from django.template import loader
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

import requests
import os
import json

from .forms import URLForm


def index(request):
    short_link = ""
    long_link = ""
    error = ""
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            bit_response = get_short_url(form.cleaned_data["url_input"])
            if "error" in bit_response:
                error = bit_response["error"]
            else:
                short_link = bit_response["link"]
                long_link = bit_response["long_url"]
            form = URLForm()
    else:
        form = URLForm()
    template = loader.get_template("urlshortener/index.html")
    context = {
        "form": form,
        "short_link": short_link,
        "long_link": long_link,
        "error": error,
    }
    return HttpResponse(template.render(context, request))


def get_short_url(url):
    url = url_fixer(url)
    if not url:
        return { "error": "Unable to process user input" }
    key = os.environ.get("URL_SHORTENER_KEY")
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json',
    }

    data = {
        "long_url": url,
    }

    return requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=json.dumps(data)).json()


def url_fixer(url):
    validate = URLValidator()
    if "://" not in url:
        url = f"https://{url}"
    try:
        validate(url)
        return url
    except:
        print("URL did not look good")
        return False
