from flask import Flask,render_template,request,redirect
from controlador_cotizacion import ControladorCotizacion

controlador = ControladorCotizacion()
app = Flask(__name__)

cantidad_ventanas = 0

@app.route("/")
def index():
    
    global cantidad_ventanas
    modelos = controlador.data["estilo_naves"]
    acabados = controlador.data["costo_por_cm_lineal"]
    vidrio = controlador.data["costo_por_cm2"]
    cantidad_ventanas = 0
    return render_template('index.html',modelos=modelos,acabados=acabados,vidrio=vidrio)

@app.route("/procesar_cotizacion", methods=["POST"])
def procesar_cotizacion():
    global cantidad_ventanas
    if request.method == "POST":
        ventanas = []
        nombre_cliente = request.form["nombre"]
        empresa_cliente = request.form["empresa"]
        modelo = request.form["modelo"]
        acabado = request.form["acabado"]
        tipo_vidrio = request.form["vidrio"]
        esmerilado = request.form["esmerilado"]
        ancho = request.form["ancho"]
        alto = request.form["alto"]
        cantidad = request.form["cantidad"]
        ventana = controlador.agregar_ventanas(modelo, ancho, alto, acabado, tipo_vidrio, cantidad, esmerilado)
        ventanas.append(ventana)
        
        continuar = request.form["otro_modelo"]
        continuar = continuar.upper()
        cantidad_ventanas += int(cantidad)
        
        if continuar == "NO":
            cliente = controlador.agregar_cliente(nombre_cliente, empresa_cliente, cantidad_ventanas)
            controlador.crear_cotizacion(cliente, ventanas)
            total = controlador.total
            vntnas = controlador.obtener_ventanas()
            print(f"Totales: {total}, cantidad ventanas {cantidad_ventanas}")
            print(f"Subtotal: {total[0]}")
            sub_total = total[0]
            descuento = total[1]
            iva = sub_total*19/100
            total_general = sub_total-descuento+iva
            totales =[sub_total,descuento,iva,total_general]
            controlador.clear_lists()
            return render_template("mostrar_cotizacion.html",nombre=nombre_cliente,empresa=empresa_cliente,total=totales,ventanas=vntnas,cantidad=cantidad_ventanas)
        else:
            modelos = controlador.data["estilo_naves"]
            acabados = controlador.data["costo_por_cm_lineal"]
            vidrio = controlador.data["costo_por_cm2"] 
            return render_template('index.html',modelos=modelos,acabados=acabados,vidrio=vidrio,nombre=nombre_cliente,empresa=empresa_cliente)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000, debug=True)