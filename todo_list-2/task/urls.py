from django.urls import path
from task import views

urlpatterns = [
    path("", views.index, name='home'),
    
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),

    # CRUD routs

    path("add-task", views.create_task, name='add-task'),   # Create
    path("task-list", views.task_list, name='task-list'),   # Retrieve all
    path("task/<int:id>", views.task_detail, name='task-detail'),  # Retrieve one
    path("edit-task/<int:id>", views.update_task, name='edit-task'), # Update
    path("remove-task/<int:id>", views.delete_task, name='remove-task'), # Delete

]

