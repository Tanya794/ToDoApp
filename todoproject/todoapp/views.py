from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import ToDoListItem


# Create your views here.
def todoappView(request):
    all_items = ToDoListItem.objects.all()
    return render(request, 'todoapp/todolist.html', context={'all_items': all_items})


def addTodoView(request):
    x = request.POST['content']
    new_item = ToDoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')


def deleteTodoView(request, i):
    y = ToDoListItem.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')
