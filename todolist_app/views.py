from django.shortcuts import render, redirect 
from django.http import HttpResponse
from todolist_app.models import Tasklist 
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def todolist (request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("New task is added."))    
        return redirect('todolist')
    else:
        allTask = Tasklist.objects.all()
        paginator = Paginator(allTask, 5)
        page = request.GET.get('pg')
        allTask = paginator.get_page(page)
        return render(request,'todolist.html', {'allTask': allTask})

def delete_task (request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.delete()

    return redirect('todolist')    

def edit_task (request, task_id):
    if request.method == "POST":
        task = Tasklist.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task is edited."))    
        return redirect('todolist')
    else:
        task_obj = Tasklist.objects.get(pk=task_id)
        return render(request,'edit.html', {'task_obj': task_obj})
    
def complete_task (request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done = True
    task.save()

    return redirect('todolist')

def pending_task (request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done = False
    task.save()

    return redirect('todolist')

def index (request):
    context = {
        'index_text': "Welcome to index."
    }
    return render(request,'index.html', context)

def contact (request):
    context = {
        'contact_text': "Welcome to contact."
    }
    return render(request,'contact.html', context)

def about (request):
    context = {
        'about_text': "Welcome to about."
    }
    return render(request,'about.html', context)
