import json

try:
    with open("biblioteca.json", "r") as archivo:
        biblioteca = json.load(archivo)
except FileNotFoundError:
    biblioteca = []


print ("*****************************")
print ("*       MUNDO LIBRO          *")
print ("*****************************")
print("[1]","-" "Mantenedor de libros")
print("[2]","-" "Reportes")
print("[3]", "Salir")

opcion = int(input("Ingresa la opción que desees: "))

if opcion == 1:
    
    print ("*****************************")
    print ("*       MUNDO LIBRO          *")
    print ("*****************************")
    print("[1]","-" "Agregar libro")
    print("[2]","-" "Editar libro")
    print("[3]","-","Eliminar libro")
    print("[4]","-" "Buscar libro")
    print("[5]","-" "Volver")
    
    opcionsegunda = int(input("Ingresa la opción que desees: "))

    if opcionsegunda == 1:
        titulo = input("Ingresa el título del libro: ")
        autor_id = input("Ingresa el AutorID: ")
        categoria_id = input("Ingresa la CategoríaID: ")
        ano_publicacion = input("Ingresa el Año de Publicación: ")

        nuevo_libro = {
            "Titulo": titulo,
            "AutorID": autor_id,
            "CategoriaID": categoria_id,
            "AnoPublicacion": ano_publicacion
        }

        biblioteca.append(nuevo_libro)

       
        with open("biblioteca.json", "w") as archivo:
            json.dump(biblioteca, archivo, indent=4)

        print(f"Libro '{titulo}' añadido exitosamente.")
    for libros in biblioteca:
        print([libros])