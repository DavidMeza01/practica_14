contactos = {}
print ("Hecho por David Meza Rincon")
def agregar_contacto():
    nombre = input("nombre del producto: ")
    telefono = input("marca del producto: ")
    email = input("contenido neto del producto: ")
    direccion = input("color del producto: ")
    cumpleaños = input("sabor(dulce,acido,picante) ")
    empresa = input("estado de agregacion(solido,liquido,gas)" )
    puesto = input("medidas del producto: ")
    notas = input("numero de sellos alimenticios: ")
    sitio_web = input("envase del producto(lata,bolsa,etc) ")
    otro_telefono = input("categoria del producto(fritura,pastel,jugo) ")
    
    contactos[nombre] = {
        'nombre del producto': nombre,
        'marca del producto': telefono,
        'Contenido neto del producto': email,
        'color del producto': direccion,
        'sabor del producto': cumpleaños,
        'consistencia del producto': empresa,
        'medidas del producto': puesto,
        'numero de sellos alimenticios': notas,
        'categoria del producto': otro_telefono
    }
    print(f"producto {nombre} agregado.")
    print("base de datos desarrollada por roberto torres toriz y david meza ricon")

def mostrar_contactos():
    if contactos:
        for nombre, detalles in contactos.items():
            print(f"\nNombre: {nombre}")
            for clave, valor in detalles.items():
                print(f"{clave}: {valor}")
    else:
        print("No hay productos.")

def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        print(f"producto {nombre} eliminado.")
    else:
        print(f"No se encontró el producto: {nombre}")

while True:
    print("\nAgenda de productos")
    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Eliminar producto")
    print("4. Salir")

    opcion = input("Elige una opción (1/2/3/4): ")
    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        mostrar_contactos()
    elif opcion == "3":
        nombre = input("Nombre del contacto a eliminar: ")
        eliminar_contacto(nombre)
    elif opcion == "4":
        print("Saliendo de la agenda.")
        break
    else:
        print("Opción inválida")