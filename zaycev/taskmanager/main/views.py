from django.shortcuts import render, redirect
from .models import Clinic
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    clinics = Clinic.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks, 'clinics': clinics})


def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной '

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

