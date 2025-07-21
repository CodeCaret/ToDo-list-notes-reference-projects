from django.shortcuts import render

def index(request):
    context = {
        'title': 'ToDo World',
    }
    return render(request, 'index.html', context)


tasks = [
    {
        'id':1,
        'title':'Python Revision',
        'about':'Go over Object-Oriented Programming (OOP) concepts in Python. Focus on classes, inheritance, polymorphism, and encapsulation.',
    },
    {
        'id':2,
        'title':'Django Practice',
        'about':"Practice Django's core concepts by exploring template inheritance, dynamic URLs, and static files management. Create a base template with common layout elements, define dynamic URLs with parameters, and properly serve static assets like CSS and JavaScript in your project.",
    },
    {
        'id':3,
        'title':'Organize Desktop Files',
        'about':'Clean up and categorize files on the desktop. Move documents, images, and other files into appropriate folders.',
    },
    {
        'id':4,
        'title':'Prepare Budget Spreadsheet',
        'about':'Create a spreadsheet to track monthly income and expenses. Categorize expenditures and set budget limits for each category.',
    },
    {
        'id':5,
        'title':'Practice Meditation for 10 Minutes',
        'about':'Spend 10 minutes practicing mindfulness or guided meditation. Focus on your breath and clear your mind of distractions.',
    },
    {
        'id':6,
        'title':'Plan Weekend Getaway',
        'about':'Research and plan a weekend trip. Look into accommodation options, travel routes, and things to do at the destination.',
    },
]

def task_list(request):
    context = {
        'title':'Task List',
        'tasks':tasks,
    }
    return render(request, 'task_list.html', context)


def task_detail(request, id):
    specific_task = None
    for task in tasks:
        if task['id'] == id:
            specific_task = task
            break
    context = {
        'title':'Task Detail',
        'task':specific_task,
    }
    return render(request, 'task_detail.html', context)


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