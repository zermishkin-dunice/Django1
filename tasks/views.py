from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import TemplateView


class AboutView(TemplateView):
    def update_data(self):
        self.tasks = Task.objects.all()
        self.dones = Task.objects.filter(is_done=True)
        self.not_dones = Task.objects.filter(is_done=False)
        self.form_for_create = TaskForm()

    def get(self, request):
        self.update_data()
        return render(request, 'index_5.html', {'tasks': self.tasks, 'dones': self.dones,
                                                'not_dones': self.not_dones, 'form_for_create': self.form_for_create})

    def post(self, request):
        self.update_data()
        new_title = request.POST.get("title")
        new_desc = request.POST.get("desc")
        id = request.POST.get("id")
        if (id == None):
            form = TaskForm(data=request.POST)
            if form.is_valid():
                form.save()
                
            return redirect('task_list')
        else:
            if ("delete" in request.POST):
                delete_task = Task.objects.get(pk=id)
                delete_task.delete()
                return redirect('task_list')
            edit_task = Task.objects.get(pk=id)
            form = TaskForm(data=request.POST, instance=edit_task)
            form.save()
            return redirect('task_list')
