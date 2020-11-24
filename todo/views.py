from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Todo
from .forms import TaskForm


def index(request):
    form = TaskForm()
    if request.method == "POST":
        if "del" in request.POST:
            Todo.objects.get(pk=request.POST["del"]).delete()
        if "pause" in request.POST:
            temp = Todo.objects.get(pk=request.POST["pause"])
            temp.paused = True
            temp.save()
        if "complete" in request.POST:
            temp = Todo.objects.get(pk=request.POST["complete"])
            temp.complete = True
            temp.paused = False
            temp.save()
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task_title"]
            Todo.objects.create(title=task, complete=False, paused=False)
            form = TaskForm()
        else:
            form = TaskForm()
        return HttpResponseRedirect(request.path_info)
    pause_bar = 0
    complete_bar = 0
    task_list = Todo.objects.order_by("-date").filter(complete=False, paused=False)
    pause_list = Todo.objects.order_by("-date").filter(paused=True)
    complete_list = Todo.objects.order_by("-date").filter(complete=True)
    sum_list = len(task_list) + len(pause_list) + len(complete_list)
    if sum_list > 0:
        pause_bar = str(((len(pause_list) + len(complete_list)) / sum_list)*100) + "%"
        complete_bar = str((len(complete_list) / (sum_list))*100) + "%"
    template = loader.get_template("todo/index.html")
    context = {
        "tasks": task_list,
        "paused": pause_list,
        "complete": complete_list,
        "form": form,
        "complete_bar": complete_bar,
        "pause_bar": pause_bar,
    }
    return HttpResponse(template.render(context, request))
