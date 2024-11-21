from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Task


def menu(request):
    return render(request, 'to_do_list/menu/menu.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Verifica se o nome de usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "Nome de usuário já está em uso")
            return redirect('register_user')

        # Verifica se o e-mail já está registrado
        if User.objects.filter(email=email).exists():
            messages.error(request, "E-mail já está em uso")
            return redirect('register_user')

        # Cria o novo usuário
        user = User.objects.create_user(username=username, email=email)
        user.save()

        messages.success(request, f"Cadastro realizado com sucesso!")
        return redirect('menu')

    return render(request, 'to_do_list/register_user/register.html')


def create_task(request):
    users = User.objects.all()

    if request.method == 'POST':
        description = request.POST.get('description')
        department_name = request.POST.get('department_name')
        priority = request.POST.get('priority')
        username = request.POST.get('username')

        user = User.objects.filter(username=username).first()

        Task.objects.create(
            description=description,
            department_name = department_name,
            priority=priority,
            user=user
        )

        messages.success(request, "Tarefa criada com sucesso!")
        return redirect('menu')

    context = {
        'users': users
    }   

    return render(request, 'to_do_list/tasks/create_task.html', context)


def manage_tasks(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks
    }
    return render(request, 'to_do_list/tasks/manage_tasks.html', context)


def update_task(request, environment_id, task_id):

    return render(request, 'to_do_list/tasks/manage_tasks.html')


def delete_task(request, environment_id, task_id):
    task = Task.objects.filter(id=task_id).first()

    if request.method == 'POST':

        task.delete()
        messages.success(request, 'Tarefa deletada com sucesso!')
        return redirect('environment', environment_id)
    
    if task:
        context = {
            'task': task
        }
    else:
        messages.error('Tarefa não encontrada!')
        context={}

    return render(request, 'to_do_list/tasks/delete_task.html', context)