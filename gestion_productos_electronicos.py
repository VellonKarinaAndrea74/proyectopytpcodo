# ** Este codigo lo hice nuevo y con tematica "Gestion de productos Electronicos"
# Uso de import csv(valores separados por comas)
# import os (importa el modulo para interactuar con el sistema operativo)#
# en este caso,es para verificar si el archivo csv existe antes de intentar cargar datos desde el mismo 
import csv
import json
import os
from datetime import datetime



# **  Usuario y  Contraseña para ingresar a la aplicacion
# Variables
usuarios_validos = {"DonPepito": "redificil123", "DonJose": "clavedificult456"}


# ** Puse un while para intentos cuando ingresas para iniciar sesion , pero no se si es correcto...
def iniciar_sesion():
    intentos = 3  # Número de intentos permitidos
    while intentos > 0:
        nombre = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

        if nombre in usuarios_validos and password == usuarios_validos[nombre]:
            print(f"Bienvenido, {nombre}! Puedes ingresar a la aplicación 😎")
            break  # Romper el bucle porque son correctas
        else:
            intentos -= 1
            print(
                f"Usuario o clave ingresada son incorrectas. Intentos restantes: {intentos}"
            )

    if intentos == 0:
        print("Número máximo de intentos ingresados 😫❌📛🛑, intentelo nuevamente...")
        # return False  # Usuario no  (probar , por el momento dejar en suspenso)


# Ejecutar función para iniciar sesión
iniciar_sesion()

# Lista de diccionarios con su id correspondiente
inventario = [
    {"id": 1, "nombre": "Producto1", "campo1": "Valor1", "campo2": "Valor2"},
    {"id": 2, "nombre": "Producto2", "campo1": "Valor3", "campo2": "Valor4"},
    {"id": 3, "nombre": "Producto3", "campo1": "Valor5", "campo2": "Valor6"},
    {"id": 4, "nombre": "Producto4", "campo1": "Valor7", "campo2": "Valor8"},
    {"id": 5, "nombre": "Producto5", "campo1": "Valor9", "campo2": "Valor10"},
]


# Función para agregar un nuevo producto al inventario

def agregar_producto(inventario):
#inventario.append({"nombre":nombre,"cantidad":cantidad, "precio":precio, "fecha":fecha})
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad disponible: "))
    precio = float(input("Precio por unidad: "))
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    producto = {'nombre': nombre, 'cantidad': cantidad, 'precio': precio, 'fecha': fecha}
    inventario.append(producto)
    print(f"{nombre} ha sido agregado al inventario.")


# Función para mostrar el inventario
def mostrar_inventario(inventario):
    print("🔷🔻" * 25)
    for producto in inventario:
        print(
            f"{producto['nombre']} - Cantidad: {producto['cantidad']}, Precio: ${producto['precio']}, Fecha: {producto['fecha']}"
        )
     

# Función para buscar un producto por nombre
def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print(
                f"Producto encontrado: {producto['nombre']} - Cantidad: {producto['cantidad']}, Precio: ${producto['precio']}, Fecha: {producto['fecha']}"
            )
            return
    print(f"Producto no encontrado con el nombre {nombre}.")
     
    
    
# Función para realizar una venta
def vender_producto(inventario, nombre, cantidad):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            if producto["cantidad"] >= cantidad:
                producto["cantidad"] -= cantidad
                guardar_inventario(inventario)
                print(
                    f"Venta realizada: {cantidad} unidades de {producto['nombre']} por ${cantidad * producto['precio']}."
                )
                return
            else:
                print(f"No hay suficientes unidades de {producto['nombre']} en stock.")
                return
    print(f"Producto no encontrado con el nombre indicado ❌🔴 {nombre}.")
    

# Función para guardar el inventario en un archivo CSV
def guardar_inventario(inventario):
    with open("inventario.csv", "w", newline="") as csvfile:
        fieldnames = ["nombre", "cantidad", "precio", "fecha"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for producto in inventario:
            writer.writerow(producto)
    
    
    
# Guardar el inventario en formato JSON
nombre_archivo_json = "inventario.json"
with open(nombre_archivo_json, "w") as json_file:
        json.dump(inventario, json_file)           

# Función para eliminar producto del inventario en un archivo CSV           
def eliminar_producto(inventario):
    id_a_eliminar = int(input("Ingrese el ID del producto a eliminar: "))
    inventario[:] = [producto for producto in inventario if producto["id"] != id_a_eliminar]
    print("¡Producto eliminado con éxito!")  


# Función para editar la información de un producto existente
def editar_producto(inventario):
    id_a_editar = int(input("Ingrese el ID del producto a editar: "))
    for producto in inventario:
        if producto["id"] == id_a_editar:
            print(f"Editando información del producto {producto['nombre']}:")
            producto["nombre"] = input("Nuevo nombre: ")
            producto["cantidad"] = int(input("Nueva cantidad: "))
            producto["precio"] = float(input("Nuevo precio por unidad: "))
            print("Información editada con éxito.")
            return
    print(f"Producto no encontrado con el ID {id_a_editar}.") 

# Función para validar la entrada del usuario (números enteros)
def obtener_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")   
  
  
# Lista de inventario con su id correspondiente
inventario = []   


# Función principal y bucle principal
# Función principal
def main():
    # Cargar el inventario desde el archivo CSV
    inventario = []
    if os.path.exists("inventario.csv"):
        with open("inventario.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                inventario.append(row)

def main():
    while True:
        print("🔷🔺" * 25)
        print("\n---- Menú de Gestión de Stock ----")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Vender producto")
        print("5. Guardar producto")
        print("6. Eliminar producto")
        print("7. Editar Producto")
        print("8. Salir")
        
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
            buscar_producto(inventario, nombre_buscar)
        elif opcion == "4":
            nombre_vender = input("Ingrese el nombre del producto a vender ✍🏽☑: ")
            cantidad_vender = int(input("Ingrese la cantidad a vender ✍🏽☑: "))
            vender_producto(inventario, nombre_vender, cantidad_vender)
        elif opcion == "5":
            guardar_inventario(inventario)        
        elif opcion == "6":
            eliminar_producto(inventario)
        elif opcion == "7":
            editar_producto(inventario) 
        elif opcion == "8":       
            print("Saliendo del programa. ¡Hasta luego! 👋🏽")
            break
        else:
            print("Opción Incorrecta ❗😥. Por favor, ingrese un número válido.") 

if __name__ == "__main__":
    main()

# Guardar el inventario en formato JSON
nombre_archivo_json = "inventario.json"
with open(nombre_archivo_json, "w") as json_file:
        json.dump(inventario, json_file)   















       




