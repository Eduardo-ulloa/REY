lista_compra = [
    {"nombre":"Mango","precio":5000,"cantidad":3},
    {"nombre":"Frutilla","precio":3500,"cantidad":4},
    {"nombre":"Bebida","precio":6000,"cantidad":2},
]

op_menu = [
    "1. comprar producto",
    "2. mostrar compra",
    "3. salir "
]

def mostrar_menu(op_menu):
    print("=== MENU LISTA DE COMPRA ===")
    
    for opcion in op_menu:
        print(opcion)

def pedir_opcion(op_max):
    seguir = True
    
    while seguir:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion <1 or opcion > op_max:
                print("ERROR. opcion invalida")
            else:
                seguir = False
        except:
            print(f"ERROR: debe ser un valor numerico entre 1 {op_max}") 
    return opcion  

def comprar_producto(lista_compra):
    nombre = "" 
    
    while nombre.strip() == "":
        nombre = input("Ingrese nombre del producto: ")
        
        if nombre.strip() == "":
            print("ERROR: el nombre no puede estar vacio")
    
    seguir = True
    
    while seguir:
        try:
            precio = int(input("Ingrese precio: "))
            
            if precio >0 :
                seguir = False
            else:
                print("ERROR: El precio debe ser mayor a 0")
        except:
            print("Debe ingresar un numero")

    
    seguir = True
    
    
    while seguir:
        try:
            cantidad = int(input("Ingrese cantidad: "))
            
            if cantidad > 0:
                seguir = False
            else:
                print("ERROR: la cantidad debe ser mayor a 0")
        except:
            print("Debe ingresar un numero")
    
    lista_compra.append({
        "nombre": nombre.strip(),
        "precio": precio,
        "cantidad": cantidad
    })     
    print("Producto agregado correctamente")
    return lista_compra

def validar_descuento(total):
    descuento = 0
    
    if total >100000:
        descuento = total * 0.20
    elif total > 50000:
        descuento = total* 0.10
    elif total > 20000:
        descuento = total * 0.05
    return descuento

def mostrar_compra(lista_compra):

    if len(lista_compra) == 0:
        print("No hay productos registrados")
        return
    
    total = 0

    print("=== Lista de compra ===")
    print("Producto\tTotal")

    for producto in lista_compra:
        subtotal = producto["precio"] * producto["cantidad"]
        total += subtotal

        print(f"{producto["nombre"]}\t{subtotal}")

    descuento = validar_descuento(total)

    print("============================")
    print(f"Total: {total}")

    if descuento > 0:
        print(f"Descuento: {descuento}")
    print(f"Total a pagar: {total - descuento}")

###
opcion = 0

while opcion != len(op_menu):
    mostrar_menu(op_menu)
    
    opcion = pedir_opcion(len(op_menu))
    
    match opcion:
        case 1:
            lista_compra = comprar_producto(lista_compra)
        case 2:
            mostrar_compra(lista_compra)
        case 3:
            print("Programa finalizado")
    
        

           
