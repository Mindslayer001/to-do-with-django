from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoForm

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'toDo/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'toDo/add_todo.html', {'form': form})

def complete_todo(request, todo_id):
    todo = TodoItem.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

def delete_todo(request, todo_id):
    todo = TodoItem.objects.get(pk=todo_id)
    todo.delete()
    return redirect('todo_list')

def edit_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, pk=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'toDo/edit_todo.html', {'form': form})