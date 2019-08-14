from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'desc', 'id', 'is_done')

    def __init__(self, *args, **kwargs):
        # Arguments must be set, because without them the form does not work
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].label = 'Название таска'
        self.fields['desc'].widget.attrs.update({'class': 'form-control'})
        self.fields['desc'].label = 'Описание таска'
        self.fields['is_done'].label = 'Выполнено'
