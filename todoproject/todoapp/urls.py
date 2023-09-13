from django.urls import path
from . import views

urlpatterns = [
    path('todoapp/', views.todoappView),
    path('addTodoItem/', views.addTodoView),
    path('deleteTodoItem/<int:i>/', views.deleteTodoView),
]