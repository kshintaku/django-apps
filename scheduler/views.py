from datetime import datetime
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.template import loader

from .models import Event
from .utils import Calendar


def index(request):
    dt = datetime.now()
    cal = Calendar(dt.year, dt.month).format_month()

    template = loader.get_template("scheduler/index.html")
    print(mark_safe(cal))
    context = {
        "calendar": mark_safe(cal),
    }
    return HttpResponse(template.render(context, request))
