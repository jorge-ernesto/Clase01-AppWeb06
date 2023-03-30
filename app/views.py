from django.shortcuts import render,redirect
from .forms import AgregarTarea

tareas=[]
# Create your views here.
def home(request):
    contexto={'tareas':tareas}
    return render(request,'app/home.html',contexto)

def adicionar(request):
    if request.method=='POST':
        form=AgregarTarea(request.POST)
        if form.is_valid():
            tarea=form.cleaned_data['tarea']
            tareas.append(tarea)
            return redirect('home')
    else:
        form=AgregarTarea()
    contexto={'form':form}
    return render(request,'app/adicionar.html',contexto)


