

'''Este ejemplo utiliza clases para representar productos y una tienda. 
La tienda puede agregar productos a su inventario, realizar compras y mostrar el inventario actualizado. 
Ten en cuenta que esta es una simulación básica y no incluye detalles avanzados de una tienda real, como gestión de dinero, autenticación, etc.'''

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Tienda:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, producto, cantidad):
        if producto in self.inventario:
            self.inventario[producto] += cantidad
        else:
            self.inventario[producto] = cantidad

    def comprar(self, producto, cantidad):
        if producto in self.inventario and self.inventario[producto] >= cantidad:
            self.inventario[producto] -= cantidad
            return f"Has comprado {cantidad} unidades de {producto.nombre}"
        else:
            return "Producto no disponible o cantidad insuficiente en inventario"

    def mostrar_inventario(self):
        print("Inventario:")
        for producto, cantidad in self.inventario.items():
            print(f"{producto.nombre} - Cantidad: {cantidad}")

# Crear productos
producto1 = Producto("Camiseta", 20)
producto2 = Producto("Pantalón", 30)
producto3 = Producto("Zapatos", 50)

# Crear tienda
tienda = Tienda()

# Agregar productos al inventario de la tienda
tienda.agregar_producto(producto1, 10)
tienda.agregar_producto(producto2, 5)
tienda.agregar_producto(producto3, 3)

# Mostrar inventario inicial
tienda.mostrar_inventario()

# Simulación de compra
print(tienda.comprar(producto1, 2))
print(tienda.comprar(producto2, 1))
print(tienda.comprar(producto3, 2))
print(tienda.comprar(producto2, 5))

# Mostrar inventario después de las compras
tienda.mostrar_inventario()





