from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import ToDoListItem
from .forms import TaskToDo


# Create your views here.
def todoappView(request):
    form = TaskToDo()
    all_items = ToDoListItem.objects.all()
    return render(request, 'todoapp/todolist.html', context={'all_items': all_items, 'form': form})


def addTodoView(request):
    new_item = ToDoListItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todoapp/')


def delete_them(request):
    x = request.POST
    for k in x:
        if k.isnumeric():
            y = ToDoListItem.objects.get(id=int(k))
            y.delete()
    return HttpResponseRedirect('/todoapp/')

