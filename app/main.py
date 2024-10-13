from controlador_cotizacion import ControladorCotizacion

#Listas para generear los menus de seleccion
modelos_ventana = ["O","XO","OXO","OXXO"]
aluminio = ["Pulido","Lacado Brillante","Lacado Mate","Anodizado"]
vidrio_list = ["Transparente","Bronce", "Azul"]
esmerilado_lst = ["Si","No"]

controlador = ControladorCotizacion()

def mostrar_menu():
    print("1. Crear cotización")
    print("2. Salir")

def pedir_opciones(opciones,inf):
    while True:
        for i, opcion in enumerate(opciones):
            print(f"{i}. {opcion}") 
        try:
            opc = int(input("Digite su opcion: "))
            if 0 <= opc < len(opciones):
                break
            else:
                    print("")
                    print("Digite una opcion valida del menu!!")
                    print(inf)
                    print("")
        except ValueError:
            print("")
            print("Digite una opcion valida del menu!!")
            print(inf)
            print("")
    return opc  

def pedir_numeros(opcion):
    while True:
        try:
            opc = int(input(f"Digite {opcion}: "))
            if opc >= 0:
                break
            else:
                    print("")
                    print(f"Digite {opcion} valido!!")
                    print("")
        except ValueError:
            print("")
            print(f"Digite {opcion} valido!!")
            print("")
    return opc  

def pedir_datos():    
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    empresa_cliente = input("Ingrese el nombre de la empresa: ")
    cantidad_ventanas = 0
    resp = "S"
    ventanas = []
    while resp == "S":
        print("Escoja el modelo de la ventana")
        cod_estilo_ventana = pedir_opciones(modelos_ventana,"Escoja el modelo de la ventana")
        estilo = modelos_ventana[cod_estilo_ventana]
        print()
        print("Escoja el tipo de acabado del aluminio")
        cod_tipo_acabado_aluminio = pedir_opciones(aluminio,"Escoja el tipo de acabado del aluminio")
        acabado = aluminio[cod_tipo_acabado_aluminio]
        print()
        print("Escoja el tipo de vidrio")
        cod_tipo_vidrio = pedir_opciones(vidrio_list,"Escoja el tipo de vidrio")
        tipo_vidrio=vidrio_list[cod_tipo_vidrio]
        print("Desea el vidrio esmerilado S=Si/N=No:")
        esm = pedir_opciones(esmerilado_lst,"Desea el vidrio esmerilado S=Si/N=No:")
        esmerilado = True if esm == 0 else False
        ancho = pedir_numeros("el ancho de la ventana")
        alto = pedir_numeros("el alto de la ventana")
        cantidad = pedir_numeros("la cantidad de ventanas")
        cantidad_ventanas += cantidad
        print()
        ventana = controlador.agregar_ventanas(estilo, ancho, alto, acabado, tipo_vidrio, cantidad, esmerilado)
        ventanas.append(ventana)
        #print(estilo,acabado,tipo_vidrio)
        resp = input("Desea cotizar otro modelo de ventana para este cliente? <S/N>: ")
        resp = resp.upper()
        if resp.upper() == 'N':
            resp = 'N'
        
    #print(f"ventanas {ventanas}, cantidad {cantidad_ventanas}")
    cliente = controlador.agregar_cliente(nombre_cliente,empresa_cliente,cantidad_ventanas)
    controlador.crear_cotizacion(cliente,ventanas)
    total = controlador.total
    vntnas = controlador.obtener_ventanas()
    return (vntnas,nombre_cliente,empresa_cliente,cantidad_ventanas,total)

def mostrar_cotizacion(datos):
    vntnas,nombre_cliente,empresa_cliente,cantidad_ventanas,total = datos
    print()
    print(f"Nombre: {nombre_cliente}")
    print(f"Empresa: {empresa_cliente}")
    print("DETALLE DE LA COTIZACION")
    ancho_col = 68
    print('='*ancho_col)
    formato_cols = '{0:<7} {1:<20} {2:<15} {3:<6} {4:<6} {5:<6}'
    print(formato_cols.format('Modelo', 'Aluminio', 'Vidrio', 'Ancho', 'Alto', 'Cantidad'))
    print('='*ancho_col)
    #print(vntnas)
    for ven in vntnas:
        #print(ven[3])
        print(formato_cols.format(ven[0],ven[3],ven[4],ven[1],ven[2],ven[5]))
    
    print()
    print(f"Cantidad de ventanas cotizadas: {cantidad_ventanas}")
    print(f"El costo total de la cotización es: ${total:.0f}")
    print()
    x=input("Presione <enter> para contunuar ")
    print()

def principal():
    while True:
        controlador.clear_lists()
        mostrar_menu()
        opc = input("Seleccione una opcion: ")
        if opc == '1':
            datos=pedir_datos()
            mostrar_cotizacion(datos)
        elif opc == '2':
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida, Ingtente de nuevo")

if __name__ == "__main__":
    principal()