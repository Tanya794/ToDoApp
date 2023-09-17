from django import forms
from .models import ToDoListItem


#class TaskToDo(forms.Form):
#    content = forms.CharField(max_length=40, label='')


class TaskToDo(forms.ModelForm):
    class Meta:
        model = ToDoListItem
        fields = '__all__'
        labels = {'content': ''}
