from django.shortcuts import render

from .models import Task
from .forms import TaskForm


def task_list(request):
    from django.forms import modelformset_factory

    tasks = Task.objects.all()
    dones = Task.objects.filter(is_done=True)
    not_dones = Task.objects.filter(is_done=False)
    form_for_create = TaskForm()
    


    if request.method == 'GET':
        return render(request, 'index.html', {'tasks': tasks, 'dones': dones, 'not_dones': not_dones, 'form_for_create': form_for_create})
    if request.method == "POST":
        new_title = request.POST.get("title")
        new_desc = request.POST.get("desc")
        id = request.POST.get("id")
        print(request.POST)
        if (id == None):
            print("Создаем новое задание")
            Task.objects.create(title=new_title, desc=new_desc)
        else:
            if ("delete" in request.POST):
                delete_task = Task.objects.get(pk=id)
                delete_task.delete()
                return render(request, 'index.html', {'tasks': tasks, 'dones': dones, 'not_dones': not_dones, 'form_for_create': form_for_create})
            edit_task = Task.objects.get(pk=id)
            edit_task.title = new_title
            edit_task.desc = new_desc
            if ("is_done" in request.POST):
                edit_task.is_done = True
            else:
                edit_task.is_done = False    
            edit_task.save()

        return render(request, 'index.html', {'tasks': tasks, 'dones': dones, 'not_dones': not_dones, 'form_for_create': form_for_create})
    