from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', 
        {'all_items': all_todo_items})

def addTodo(request):
    tarea = request.POST['content']
    itemNuevo = TodoItem(content = tarea)
    itemNuevo.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    tareaParaBorrar = TodoItem.objects.get(id = todo_id)
    tareaParaBorrar.delete()
    return HttpResponseRedirect('/todo/')