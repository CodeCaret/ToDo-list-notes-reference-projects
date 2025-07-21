from django.urls import path
from task import views

urlpatterns = [
    path("", views.index, name='home'),
    path("task-list", views.task_list, name='task-list'),
    path("task/<int:id>", views.task_detail, name='task-detail'),

    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
]


