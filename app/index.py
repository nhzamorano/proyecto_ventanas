from flask import Flask,render_template,request,redirect
from controlador_cotizacion import ControladorCotizacion

controlador = ControladorCotizacion()
app = Flask(__name__)



@app.route("/")
def index():
    modelos = controlador.data["estilo_naves"]
    acabados = controlador.data["costo_por_cm_lineal"]
    vidrio = controlador.data["costo_por_cm2"]
    return render_template('index.html',modelos=modelos,acabados=acabados,vidrio=vidrio)

@app.route("/procesar_cotizacion", methods=["POST"])
def procesar_cotizacion():
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
        cliente = controlador.agregar_cliente(nombre_cliente, empresa_cliente, cantidad)
        controlador.crear_cotizacion(cliente, ventanas)
        total = controlador.total
        vntnas = controlador.obtener_ventanas()
        controlador.clear_lists()
    return render_template("mostrar_cotizacion.html",nombre=nombre_cliente,empresa=empresa_cliente,total=total,ventanas=vntnas)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000, debug=True)