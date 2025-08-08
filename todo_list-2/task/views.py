from django.shortcuts import render, redirect
from task.models import Task

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

# CREATE
def create_task(request):

    if request.method == 'POST':
        title = request.POST['title']
        deadline = request.POST['deadline']
        about = request.POST['about']
        # Status is a checkbox field, if checked 'status' key will be created with value 'true' otherwise None so need to use .get() to avoid key error.
        # To get True or False value compare the value
        status = request.POST.get('status') == 'true'

        Task.objects.create(
            title = title,
            deadline = deadline,
            about = about,
            status = status
        )
        return redirect('task-list')
    
    context = {
        'title':'Add Task',
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
    
    try:
        task = Task.objects.get(id = id)
    except Task.DoesNotExist:
        return redirect('task-list')
    
    if request.method == 'POST':
        task.title = request.POST['title']
        task.deadline = request.POST['deadline']
        task.about = request.POST['about']
        task.status = request.POST.get('status') == 'true'
        task.save()
        # Since, it is getting redirected to the detailed page after updation which requires specific ID to render the task.
        # So, it's needed to sent through redirect()
        return redirect('task-detail', id=id)

    context = {
        'title':'Edit Task',
        'task':task,
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

