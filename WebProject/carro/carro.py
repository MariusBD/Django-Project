class Carro:
    def __init__(self, request):
        #loguear en admin si salta key error para tener una session
        self.request=request #almacena la peticion, para poder utilizar esa peticion
        self.session=request.session #iniciamos sesion
        carro=self.session.get("carro") #construimos carro para esta session
        if not carro:
            carro=self.session["carro"]={} #la clave del dict sera el id producto, el valor sera un dict con sus carac. nombre,imagen, etc..
        #else:
        self.carro=carro

    def agregar(self, producto):
        #agregar producto si no esta en este carro
        #tipo de dato producto.id str ya que clave = str
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio": str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1 #incrementar cantidad
                    value["precio"]=float(value["precio"])+producto.precio
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro #el carro tiene que ser = al carro de la sesion
        self.session.modified=True #cada operacion que se haga agregar,eliminar es una modificacion en la session.

    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_producto(self, producto):
        for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]-1
                    value["precio"]=float(value["precio"])-producto.precio
                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    break 
    #actualizar el carro y guardar carro
        self.guardar_carro()

    def limpiar_carro(self):
        #en la sesion logueada limpiar carro
        self.session["carro"]={}
        self.session.modified=True


        








