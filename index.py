class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
class Cliente:
    def __init__(self, id_cliente, nombre, direccion, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
class Venta:
    def __init__(self, id_venta, cliente, productos):
        self.id_venta = id_venta
        self.cliente = cliente
        self.productos = productos
def agregar_producto():
    id_producto = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock inicial del producto: "))
    producto = Producto(id_producto, nombre, precio, stock)
    productos.append(producto)
    print("Producto agregado con éxito.")
def listar_productos():
    print("Lista de productos:")
    for producto in productos:
        print(f"{producto.id_producto} - {producto.nombre} - Precio: ${producto.precio} - Stock: {producto.stock}")
def realizar_venta():
    id_cliente = input("Ingrese el ID del cliente: ")
    cliente = buscar_cliente(id_cliente)
def realizar_venta():
    id_cliente = input("Ingrese el ID del cliente: ")
    cliente = buscar_cliente(id_cliente)

    if cliente:
        productos_venta = []
        while True:
            listar_productos()
            id_producto = input("Ingrese el ID del producto a vender (0 para finalizar): ")
            if id_producto == '0':
                break
            producto = buscar_producto(id_producto)
            if producto and producto.stock > 0:
                productos_venta.append(producto)
                producto.stock -= 1
            else:
                print("Producto no encontrado o sin stock disponible.")
        if productos_venta:
            id_venta = len(ventas) + 1
            venta = Venta(id_venta, cliente, productos_venta)
            ventas.append(venta)
            print("Venta realizada con éxito.")