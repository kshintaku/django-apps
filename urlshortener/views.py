from django.http import HttpResponse
from django.template import loader
import requests
import os

from .forms import URLForm


def index(request):
    short_link = ""
    long_link = ""
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            bit_response = get_short_url(form.cleaned_data["url_input"])
            # print(bit_response)
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
    }
    return HttpResponse(template.render(context, request))


def get_short_url(url):
    key = os.environ.get("URL_SHORTENER_KEY")
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json',
    }

    # data = f'{{ "long_url": {url}, "domain": "bit.ly"}}'
    data = {
        "long_url": url,
        # "domain": "bit.ly",
    }

    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data).json()
    print(response)
    return response
