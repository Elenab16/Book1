from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as login_django


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirige a la página principal después del registro
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})


def login(request):
    formulario = AuthenticationForm()

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')

            user = authenticate(request, username=usuario, password=contrasenia)
            login_django(request, user)

            return redirect('myapp')

    return render(request, 'usuarios/inicio_de_sesion.html', {"formulario": formulario})

