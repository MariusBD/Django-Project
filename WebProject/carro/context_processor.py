def importe_total(request):
    total=0
    if request.user.is_authenticated: 
         if 'carro' in request.session: #verifica que carro exista en session
            for key, value in request.session["carro"].items():
                total= total+ float(value["precio"])
    return {"importe_total":total}
