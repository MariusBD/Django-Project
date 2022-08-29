from django.urls import path
from .views import Registro, cerrar_session, login

urlpatterns = [
    path('',Registro.as_view(), name="autenticacion"), #as_view() muestra la clase Registro como una vista
    path('cerrar_session/', cerrar_session, name="cerrar_session"),
    path('login/', login, name="login"),

]