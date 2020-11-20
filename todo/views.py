from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import os
import datetime

from .models import Todo
from .forms import TaskForm


def index(request):
    status = []
    task_list = Todo.objects.order_by("-date")
    for stat in Todo.STATUS:
        status.append(stat)
    template = loader.get_template("todo/index.html")
    context = {
        "list": task_list,
        "status": status,
    }
    return HttpResponse(template.render(context, request))
