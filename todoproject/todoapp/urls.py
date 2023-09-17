from django.urls import path
from . import views

urlpatterns = [
    path('todoapp/', views.todoappView),
    path('addTodoItem/', views.addTodoView),
    path('deleteTodoItem/', views.delete_them),

]