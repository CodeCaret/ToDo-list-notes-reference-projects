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

# CREATE if Using Django Form
# Feasible if input and model fields are same and no further process required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Unpacking the form.cleaned_data dictionary
            Task.objects.create(**form.cleaned_data)
            return redirect('task-list')
    else:
        form = TaskForm()

    context = {
        'title':'Add Task',
        'form':form,
    }
    return render(request, 'create_task.html', context)


# All field extraction and data creation (Required if data processing needed before saving the data)
# def create_task(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             # Process the data on form.cleaned_data
#             title = form.cleaned_data['title']
#             deadline = form.cleaned_data['deadline']
#             about = form.cleaned_data['about']
#             status = form.cleaned_data['status']
#             # Save the data
#             Task.objects.create(
#                 title = title,
#                 deadline = deadline,
#                 about = about,
#                 status = status
#             )
#             return redirect('task-list')
#     else:
#         form = TaskForm()
#     context = { 'title':'Add Task', 'form':form, }
#     return render(request, 'create_task.html', context)


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
        form = TaskForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.deadline = form.cleaned_data['deadline']
            task.about = form.cleaned_data['about']
            task.status = form.cleaned_data['status']
            task.save()
            return redirect('task-detail', id=id)
    else:
        # Pre-fill the form manually using initial
        form = TaskForm(initial={
            'title': task.title,
            'deadline': task.deadline,
            'about': task.about,
            'status': task.status,
        })
        
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

