from django.shortcuts import render, redirect, get_object_or_404
from task.models import Task
from task.forms import TaskForm

def index(request):
    context = {
        'title': 'ToDo World',
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'title': 'About me',
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'title': 'Contact me',
    }
    return render(request, 'contact.html', context)


# CRUD Implementation

# CREATE if Using Django ModelForm class
def create_task(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:   
        form = TaskForm()

    context = {
        'title':'Add Task',
        'form':form,
    }
    return render(request, 'create_task.html', context)


# RETRIEVE
def task_list(request):

    search_query = request.GET.get('search')

    if search_query:
        tasks = Task.objects.filter(title__icontains = search_query).order_by('status', '-id')
    else:
        # Retrieves in ascending order refering to ID
        # 'tasks':Task.objects.all(),

        # To Retrieve in descending order and pending tasks at top
        tasks = Task.objects.order_by('status', '-id')

    context = {
        'title':'Task List',
        'tasks':tasks,
    }
    return render(request, 'task_list.html', context)


def task_detail(request, id):
    
    try:
        task = Task.objects.get(id = id)
    except Task.DoesNotExist:
        return redirect('task-list')
    
    context = {
        'title':'Task Detail',
        'task':task,
    }
    return render(request, 'task_detail.html', context)


# UPDATE
def update_task(request, id):

    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('task-detail', id=id)
    else:
        # Pre-fill the form using instance
        form = TaskForm(instance=task)

    context = {
        'title': 'Edit Task',
        'form': form
    }
    return render(request, 'update_task.html', context)


# DELETE
def delete_task(request, id):
    
    try:
        task = Task.objects.get(id = id)
    except Task.DoesNotExist:
        return redirect('task-list')
    
    task.delete()
    return redirect('task-list')

# ----------------------------------------------------------------

