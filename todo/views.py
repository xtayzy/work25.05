from django.shortcuts import render, redirect

# Create your views here.

from todo.models import Task


def index(request):
    tasks = Task.objects.all()
    ctx = {'tasks': tasks}

    return render(request, 'todo/index.html', context=ctx)


def add(request):
    if request.method != 'POST':
        return redirect('index')
    task = Task(
        title=request.POST['task_title'],
        description=request.POST['task_des']
    )
    task.save()
    return redirect('index')


def delete(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('index')


def done(request, id):
    task = Task.objects.get(pk=id)
    task.done = True
    task.save()
    return redirect('index')


def notdone(request, id):
    task = Task.objects.get(pk=id)
    task.done = False
    task.save()
    return redirect('index')
