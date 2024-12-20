from django.urls import path
from . import views

urlpatterns = [
    path("", views.menu, name="menu"),
    path('register/', views.register, name="register_user"),

    path('tasks/', views.manage_tasks, name="manage_tasks"),
    path('tasks/create/', views.create_task, name="create_task"),
    path('tasks/<int:task_id>/update/', views.update_task, name="update_task"),
    path('tasks/<int:task_id>/update/status/', views.update_task_status, name="update_task_status"),
    path('tasks/<int:task_id>/delete/', views.delete_task, name="delete_task"),
]