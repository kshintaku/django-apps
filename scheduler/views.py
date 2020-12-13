from datetime import datetime
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.template import loader

from .models import Event
from .utils import Calendar
from .forms import AppointmentForm


def cal_form(request, year=2020, month=1, day=1):
    form = AppointmentForm(year, month, day)
    # form.set_day(year, month, day)
    # dt = datetime.now()
    cal = Calendar(year, month).format_month()

    template = loader.get_template("scheduler/calendar.html")
    context = {
        "form": form,
        "calendar": mark_safe(cal),
    }
    return HttpResponse(template.render(context, request))


def index(request):
    if request.method == "GET":
        if 'year' in request.GET and 'month' in request.GET and 'day' in request.GET:
            return cal_form(request, int(request.GET['year']), int(request.GET['month']), int(request.GET['day']))
    dt = datetime.now()
    cal = Calendar(dt.year, dt.month).format_month()

    template = loader.get_template("scheduler/index.html")
    context = {
        "calendar": mark_safe(cal),
    }
    return HttpResponse(template.render(context, request))
