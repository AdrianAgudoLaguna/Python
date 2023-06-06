from datetime import datetime

class Cliente: 
    def __init__(self,id,id_pedido,nombre,email,pais,ciudad,tipo_de_cliente):
        self.id=id 
        self.id_pedido=id_pedido
        self.nombre=nombre 
        self.email=email
        self.pais=pais
        self.ciudad=ciudad
        self.tipo=tipo_de_cliente
    
    def info_Cliente(self):
        print(f'El cliente se llama {self.nombre} y su id es {self.id}')
        print(f'Su email es  {self.email}')
        print(f'Es de  {self.pais}')
        print(f'Vive en {self.ciudad}')
        print(f'El cliente es {self.tipo}')
        print("El cliente se ha registrado correctamente ")

class Producto(Cliente):
    def __init__(self, id,id_pedido, ciudad, nombre, email, pais, tipo_de_cliente):
        super().__init__(id,id_pedido, ciudad, nombre, email, pais, tipo_de_cliente)
    def comprar_Productos(self):
        print('')
        print('Pasamos a comprar productos:')
        print('')
        print('Tenemos 3 productos a la venta' )
        print('producto1=20€(sin contar el iva)')
        print('producto2=25€(sin contar el iva)')
        print('producto3=30€(sin contar el iva)')
        print('')
        print('Para comprar eliga el producto que quiera entre producto1, producto2 y producto3')
        print('Cuando ya quiera terminar la compra ponga terminar ')
        pedido=0
        facturación=0
        while True:
            pedidos=input('Diga los productos que quiere añadir a su lista de deseos:')
            if pedidos=='producto1':
                facturación=facturación+20
                pedido=pedido+1
                print('ha añadido el producto 1')
            elif pedidos=='producto2':
                facturación=facturación+25
                pedido=pedido+1
                print('ha añadido el producto 2')
            elif pedidos=='producto3':
                facturación=facturación+30
                pedido=pedido+1
                print('ha añadido el producto 3')
            elif pedidos=='terminar':
                break
            else:
                print('No ha pedido ningún producto')
        print(f'Ha añadido un total de {pedido} productos a su lista de deseos')
        if self.pais == 'España':
            factura=facturación*1.21
            print(f'Su factura total es de {factura} $')
        else:
            factura=facturación*1.10
            print(f'Su factura total es de {factura} $')

class Pedido(Cliente):
    def __init__(self, id, id_pedido, ciudad, nombre, email, pais, tipo_de_cliente):
        super().__init__(id, id_pedido, ciudad, nombre, email, pais, tipo_de_cliente)
    def info_Pedido(self):
        print('')
        print(f'Detalles de pedido: id_pedio - {self.id_pedido},  fecha de compra - {datetime.now()}  , nombre del cliente - {self.nombre}')
    def finalizarCompra(self):
        print('Compra finalizada')
    def facturaPDF(self):
        print(f'Su factura sera enviada en pdf a {self.email}')
    def seguimiento(self):
        print(f'Se le ha enviado un sms {self.nombre} para que pueda seguir su pedido.')
        print('')




def Cliente1():
    cliente1=Cliente(1212,12,'Adrian','adrian@gmail.com','España','Madrid','Particular')
    cliente1.info_Cliente()
    producto1=Producto(1212,12,'Adrian','adrian@gmail.com','España','Madrid','Particular')
    producto1.comprar_Productos()
    pedido1=Pedido(1212,12,'Adrian','adrian@gmail.com','España','Madrid','Particular')
    pedido1.info_Pedido()
    pedido1.finalizarCompra()
    pedido1.facturaPDF()
    pedido1.seguimiento()   
#Cliente1()


def Cliente2():
    cliente2=Cliente(1213,21,'Jesús','jesus@gmail.com','Francia','Madrid','Empresa')
    cliente2.info_Cliente()
    producto2=Producto(1213,21,'Jesús','jesus@gmail.com','Francia','Madrid','Empresa')
    producto2.comprar_Productos()
    pedido2=Pedido(1213,21,'Jesús','jesus@gmail.com','Francia','Madrid','Empresa')
    pedido2.info_Pedido()
    pedido2.finalizarCompra()
    pedido2.facturaPDF()
    pedido2.seguimiento()

Cliente2()


def Prueba_Validación():
    prueba=Cliente(13,21,'Pablo',11,'Portugal','Lisboa','Empresa')
    prueba.info_Cliente()
    prueba1=Producto(13,21,'Pablo',11,'Portugal','Lisboa','Empresa')
    prueba1.comprar_Productos()
    prueba2=Pedido(13,21,'Pablo',11,'Portugal','Lisboa','Empresa')
    prueba2.info_Pedido()
    prueba2.finalizarCompra()
    prueba2.facturaPDF()
    prueba2.seguimiento()

    
#Prueba_Validación()

    

    