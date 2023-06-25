from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
<<<<<<< HEAD
from django.urls import reverse
from accounts.models import Profile
from .forms import CustomUserCreationForm,PerfilForm
from django.contrib.auth import authenticate, login



def home(request):
    return render(request,'tasks/home.html')
@login_required
def Perfil(request):
    user = request.user  # Obtener el usuario actualmente autenticado

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        form1 = PerfilForm(request.POST)
        if form.is_valid() and form1.is_valid():
            # Guardar los datos del formulario en la base de datos
            form.save()

            # Redireccionar al detalle del perfil
            return redirect('perfil')
    else:
        form = CustomUserCreationForm(initial={
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        })
        

    return render(request, 'tasks/Perfil.html', {'form': form, 'user': user})
=======
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login


def home(request):
    return render(request,'tasks/home.html')
@login_required
def mascotas(request):
    return render(request,'tasks/mascotas.html')
>>>>>>> f37be34e12396f6c2c65534768d11806d03a7709

def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            
            return redirect('home')
    return render(request,'registration/register.html', data)
<<<<<<< HEAD

def nosotros(request):
    return render(request,'tasks/nosotros.html')




def detalle_perfil(request):
    user = request.user  # Obtener el usuario actualmente autenticado

    if request.method == 'POST':
        form = PerfilForm(request.POST)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.user = user
            perfil.save()
            return redirect('detalle_perfil')
    else:
        form = PerfilForm()

    return render(request, 'tasks/detalle_perfil.html', {'form': form, 'user': user})

def NMascotas(request):
    return render(request,'tasks/NMascotas.html')

def infomascotas(request):
    return render(request,'tasks/infomascotas.html')
=======
>>>>>>> f37be34e12396f6c2c65534768d11806d03a7709
