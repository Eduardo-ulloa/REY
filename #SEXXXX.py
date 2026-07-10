#SEXXXX


libros = []

def vali_titulo(titulo):
    return titulo.strip() != ""

def vali_copias(copias):
    return copias >= 0

def vali_prestamo(prestamo):
    return prestamo > 0


def mostrar_menu():
    print("== Menú Principal ==")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")

def pedir_opcion():

    opcion = 0

    while opcion < 1 or opcion > 6:

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 6:
                print("ERROR: Debe ser una opcion del 1 al 6")

        except:
            print("ERROR: Debe ser un numero")
            opcion = 0

    return(opcion)

def posicion_libro(lista, titulo):

    for i in range(len(lista)):
        if lista[i]["titulo"].lower() == titulo.lower():
            return i

    return -1


def agregar_libro(lista):
    
    titulo = input("Ingrese titulo del libro: ")
    if vali_titulo(titulo):

        try:
            copias = int(input("Ingrese cantidad de copias: "))
        except ValueError:
            print("ERROR: Debe ingresar numero entero")
            return
        
        if vali_copias(copias):

            try:
                prestamo = int(input("Periodo de prestamo: "))
            except ValueError:
                print("ERROR: debe ingresar numero entero")
                return
            
            if vali_prestamo(prestamo):

                libro = {"titulo": titulo, "copias": copias, "prestamo": prestamo, "disponible": False}
                lista.append(libro)
                print("Libro agregado")

            else:
                print("ERROR: el periodo debe ser mayor que 0")

        else:
            print("ERROR: las copias deben ser mayor que 0")

    else:
        print("ERROR: el titulo no puede estar vacio")

def buscar_libro(lista):

    titulo = input("Ingrese el titulo del libro: ")
    posicion = posicion_libro(lista, titulo)

    if posicion != -1:
        libro = lista[posicion]

        print("== Libro Encontrado ==")
        print("Titulo:", libro["titulo"])
        print("Copias:", libro["copias"])
        print("Prestamos:", libro["prestamo"])
        print("Disponible:", libro["disponible"])
    else:
        print("Libro no encontrado")


def eliminar_libro(lista):

    titulo = input("Ingrese el libro que desea eliminar: ")

    for i in range(len(lista)):
        
        if lista[i]["titulo"].lower() == titulo.lower():
            lista.pop(i)
            return "El libro ha sido eliminado correctamente"

    return "El libro 'titulo' no se encuentra registrado"


def actualizar(lista):

    for libro in lista:

        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False
    print("Disponibilidad actualizado")


def mostrar_libros(lista):

    actualizar(lista)

    if len(lista) == 0:
        print("No hay libros registrados")
        return

    print("== Lista de libros ==")

    for libro in lista:
        if libro["disponible"]:
            estado = "Disponible"
        else:
            estado = "Sin copias"
        
        print("Titulo:", libro["titulo"])
        print("Copias:", libro["copias"])
        print("Prestamo:", libro["prestamo"])
        print("Estado:", estado)
        print("=============================")

#Programa principal

opcion = 0
while opcion != 6:

    mostrar_menu()
    opcion = pedir_opcion()

    match opcion:

        case 1:
            agregar_libro(libros)

        case 2:
            buscar_libro(libros)

        case 3:
            eliminar_libro(libros)

        case 4:
            actualizar(libros)

        case 5:
            mostrar_libros(libros)

        case 6:
            print("Programa finalizado")