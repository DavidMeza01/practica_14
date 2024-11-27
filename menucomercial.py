print("Hecho por Miguel Angel Mora Perez, Omar Perez Zarate y Jose Fernando Gonzales Muñoz")
import random
CONTRASENA = "1989"
productos = {
    "palo de golf": round(random.uniform(50, 200), 2),
    "bate": round(random.uniform(20, 100), 2),
    "balón de fútbol": round(random.uniform(10, 50), 2),
    "balón de basquetbol": round(random.uniform(15, 60), 2),
    "jerseys": round(random.uniform(25, 100), 2),
    "gorras": round(random.uniform(5, 30), 2),
    "pelotas de béisbol": round(random.uniform(3, 15), 2),
    "manopla": round(random.uniform(15, 70), 2),
    "guantes de portero": round(random.uniform(30, 150), 2),
    "tenis": round(random.uniform(40, 120), 2)
}
def mostrar_productos():
    print("Productos disponibles:")
    for producto, precio in productos.items():
        print(f"{producto.title()} - ${precio}")
def agregar_producto():
    producto = input("Ingrese el nombre del producto a agregar: ").lower()
    precio = round(random.uniform(10, 200), 2)
    productos[producto] = precio
    print(f"Producto '{producto.title()}' agregado con un precio de ${precio}.")
def modificar_producto():
    producto = input("Ingrese el nombre del producto a modificar: ").lower()
    if producto in productos:
        nuevo_precio = round(float(input(f"Ingrese el nuevo precio para '{producto.title()}': ")), 2)
        productos[producto] = nuevo_precio
        print(f"Precio de '{producto.title()}' modificado a ${nuevo_precio}.")
    else:
        print("El producto no existe.")
def eliminar_producto():
    producto = input("Ingrese el nombre del producto a eliminar: ").lower()
    if producto in productos:
        del productos[producto]
        print(f"Producto '{producto.title()}' eliminado.")
    else:
        print("El producto no existe")
def validar_contraseña():
    intento = input("Ingrese la contraseña: ")
    if intento != CONTRASENA:
        print("Contraseña incorrecta. Intente de nuevo.")
        return False
    return True
def menu():
    if not validar_contraseña():
        return
    while True:
        print("-- Menú de opciones --")
        print("1) Agregar Producto")
        print("2) Consultar Productos")
        print("3) Modificar Producto")
        print("4) Eliminar Producto")
        print("5) Salir")
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            modificar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("Gracias por usar el sistema, Adios")
            break
        else:
            print("Error")
menu()
