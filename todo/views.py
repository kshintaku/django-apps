from django.http import HttpResponse
from django.template import loader
from .models import Todo
from .forms import TaskForm


def index(request):
    form = TaskForm()
    task_list = Todo.objects.order_by("-date")
    template = loader.get_template("todo/index.html")
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task_title"]
            Todo.objects.create(title=task, complete=False, paused=False)
            form = TaskForm()
        else:
            form = TaskForm()
    context = {
        "tasks": task_list,
        "form": form,
    }
    return HttpResponse(template.render(context, request))
