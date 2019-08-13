from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'desc', 'id')

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)  #Arguments must be set, because without them the form does not work
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].label = 'Название таска'
        self.fields['desc'].widget.attrs.update({'class': 'form-control'})
        self.fields['desc'].label = 'Описание таска'
