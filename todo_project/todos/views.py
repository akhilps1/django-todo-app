from queue import Empty
from django.shortcuts import render, redirect
from . models import Todos
from .forms import TodoForm
# Create your views here.


def todos(request):
    tasks = Todos.objects.all()
    if request.method == 'POST':
        task = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        obj = Todos(task=task, priority=priority, date=date, completed=False)
        obj.save()
        return redirect('/')
    return render(request, 'index.html', {'tasks': tasks})

def update_todo(request, task_id):
    task = Todos.objects.get(id=task_id)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'task':task, 'form':form}) 
  
def delete(request, id):
    task = Todos.objects.get(id=id)
    task.delete()
    return redirect('/')

def mark_completed(request,id):
    task = Todos.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('/')
    
