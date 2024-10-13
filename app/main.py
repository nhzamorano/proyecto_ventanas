from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt
from rich.panel import Panel

from controlador_cotizacion import ControladorCotizacion

#Listas para generear los menus de seleccion
modelos_ventana = ["O","XO","OXO","OXXO"]
aluminio = ["Pulido","Lacado Brillante","Lacado Mate","Anodizado"]
vidrio_list = ["Transparente","Bronce", "Azul"]
esmerilado_lst = ["Si","No"]

controlador = ControladorCotizacion()
console = Console()

def mostrar_menu():
    menu_text = "[bold cyan]1.[/bold cyan] Crear cotización\n[bold cyan]2.[/bold cyan] Salir"
    console.print(Panel(menu_text, title="[bold green]Menú de opciones[/bold green]", expand=False))

def pedir_opciones(opciones, inf):
    while True:
        for i, opcion in enumerate(opciones):
            console.print(f"[bold cyan]{i}.[/bold cyan] {opcion}") 
        try:
            opc = int(console.input("[bold green]Digite su opción: [/bold green]")) 
            if 0 <= opc < len(opciones):
                break
            else:
                console.print("\n[bold red]¡Opción inválida![/bold red] [yellow]Por favor, digite una opción válida del menú.[/yellow]\n")
                console.print(inf) 
        except ValueError:
            console.print("\n[bold red]¡Error![/bold red] [yellow]Por favor, digite una opción numérica válida.[/yellow]\n")
            console.print(inf)
    return opc

def pedir_numeros(opcion):
    while True:
        try:
            opc = int(console.input(f"[bold green]Digite {opcion}: [/bold green]"))
            if opc >= 0:
                break
            else:
                console.print(f"\n[bold red]¡Error![/bold red] [yellow]Digite un {opcion} válido.[/yellow]\n")
        except ValueError:
            console.print(f"\n[bold red]¡Error![/bold red] [yellow]Digite un {opcion} válido.[/yellow]\n") 
    return opc

def pedir_datos():
    console.print(Panel.fit("Cotización de Ventanas", title="Sistema de Cotización", subtitle="Datos cliente y ventanas"))

    nombre_cliente = Prompt.ask("[bold cyan]Ingrese el nombre del cliente[/]")
    empresa_cliente = Prompt.ask("[bold cyan]Ingrese el nombre de la empresa[/]")
    
    cantidad_ventanas = 0
    resp = "S"
    ventanas = []
    
    while resp == "S":
        console.print(Panel("[bold yellow]Escoja el modelo de la ventana[/]"))
        cod_estilo_ventana = pedir_opciones(modelos_ventana, "Escoja el modelo de la ventana")
        estilo = modelos_ventana[cod_estilo_ventana]
        
        console.print(Panel("[bold yellow]Escoja el tipo de acabado del aluminio[/]"))
        cod_tipo_acabado_aluminio = pedir_opciones(aluminio, "Escoja el tipo de acabado del aluminio")
        acabado = aluminio[cod_tipo_acabado_aluminio]
        
        console.print(Panel("[bold yellow]Escoja el tipo de vidrio[/]"))
        cod_tipo_vidrio = pedir_opciones(vidrio_list, "Escoja el tipo de vidrio")
        tipo_vidrio = vidrio_list[cod_tipo_vidrio]

        esm = Prompt.ask("[bold cyan]¿Desea el vidrio esmerilado?[/] (S/N)").upper()
        esmerilado = True if esm == "S" else False
        
        ancho = pedir_numeros("el ancho de la ventana")
        alto = pedir_numeros("el alto de la ventana")
        cantidad = pedir_numeros("la cantidad de ventanas")
        cantidad_ventanas += cantidad
        
        ventana = controlador.agregar_ventanas(estilo, ancho, alto, acabado, tipo_vidrio, cantidad, esmerilado)
        ventanas.append(ventana)
        
        resp = Prompt.ask("[bold cyan]¿Desea cotizar otro modelo de ventana para este cliente?[/] (S/N)").upper()
        
    cliente = controlador.agregar_cliente(nombre_cliente, empresa_cliente, cantidad_ventanas)
    controlador.crear_cotizacion(cliente, ventanas)
    total = controlador.total
    vntnas = controlador.obtener_ventanas()
    print()

    return (vntnas, nombre_cliente, empresa_cliente, cantidad_ventanas, total)

def mostrar_cotizacion(datos):
    #console = Console()
    vntnas, nombre_cliente, empresa_cliente, cantidad_ventanas, total = datos
    console.print(f"[bold]Nombre:[/bold] {nombre_cliente}")
    console.print(f"[bold]Empresa:[/bold] {empresa_cliente}")

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Modelo", style="dim", width=12)
    table.add_column("Aluminio", width=20)
    table.add_column("Vidrio", width=15)
    table.add_column("Ancho", justify="right")
    table.add_column("Alto", justify="right")
    table.add_column("Cantidad", justify="right")

    for ven in vntnas:
        table.add_row(ven[0], ven[3], ven[4], str(ven[1]), str(ven[2]), str(ven[5]))

    console.print(table)

    iva = total[2] * 0.19
    total_general = total[0] + iva

    console.print(f"[bold]Cantidad de ventanas cotizadas:[/bold] {cantidad_ventanas}")
    console.print(f"[bold]Costo bruto:[/bold] ${total[2]:.0f}")
    console.print(f"[bold]Descuento:[/bold] ${total[1]:.0f}")
    console.print(f"[bold]IVA (19%):[/bold] ${iva:.0f}")
    console.print(f"[bold]Costo total:[/bold] ${total_general:.0f}")

    input("Presione <enter> para continuar ")
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