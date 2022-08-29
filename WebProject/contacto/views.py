from django.shortcuts import render,redirect
from .forms import FormContacto

from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
   
    form_contacto = FormContacto()  

    if request.method == "POST": #si se ha hecho POST
        form_contacto = FormContacto(data=request.POST) #carga en nuestro formulario la info. que el usuario ha introducido
       
        if form_contacto.is_valid():  #si se han rellenado los campos requeridos
            nombre = request.POST.get("nombre") #guarda lo que ha introducido el user
            email = request.POST.get("email")
            asunto = request.POST.get("asunto")

            email = EmailMessage("Mensaje Correo Django",
            "Nombre Usuario que envia correo {} direccion correo {} asunto: {} ".format(nombre,email,asunto),
            "",["miemail@gmail.com"])


            return redirect("/contacto/?correcto") #parametro pasado al html


            #para el email ( problemas con las politicas de gmail, para enviar)
            """try:
                email.send()   
                return redirect("/contacto/?correcto")  #feedback para el usuario
            except:
                return redirect("/contacto/?incorrecto")"""


    return render(request,"contacto/contacto.html",{"form":form_contacto})