from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import  logout, authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

class Registro(View):

    def get(self,request): #get formulario
        form = UserCreationForm() #aqui se almacena el formulario
        #renderizacion del archivo html pasandole por parametro el form
        return render(request,"autenticacion/autenticacion.html",{'form':form})
        

    def post(self,request): #envia datos a la bd
        
        form = UserCreationForm(request.POST) #almacena el user y pass

        if form.is_valid():
            usuario = form.save() #guarda la info. del form en la auth_user(bd)

            #hacer automaticamente un login al haberse registrado.
            auth_login(request, usuario) #request y usuario a loguear.
            

            return redirect('home')
        
        else: #en caso de que el user no es valido
            #recorre todos los mensajes de error que se pudieron comteter durante el fallo al introducir la pass
            for mensaje in form.error_messages:
                messages.error(request, form.error_messages[mensaje])

            #devuelve el formulario con los errores 
            return render(request,"autenticacion/autenticacion.html",{'form':form})


            
def cerrar_session(request):
    logout(request)
    return redirect('home')

def login(request):
    if request.method == "POST":
        #data = request.POST recupera el username y el password del usuario
        #introducido en el formulario login
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            #rescatamos info. del formulario
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password')

            #authenticate busca en la base de datos si el usuario existe
            user = authenticate(username = username,password=password)
            if user is not None: #si el usuario existe
                auth_login(request,user) #login
                return redirect('home')
            else:
                messages.error(request,"Este usuario no existe")
        else:
            messages.error(request, "Datos incorrectos")

    form = AuthenticationForm()
    return render(request,"autenticacion/login.html",{'form':form})












