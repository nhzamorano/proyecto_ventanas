import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.ventana import Ventana
from app.cliente import Cliente
from app.cotizacion import Cotizacion

def test_create_cotizacion():
    cliente = Cliente("Juan Perez","Aceros ZZ",10)
    ventana = Ventana('XO',15,20,'Pulido','Azul',True)
    cotizacion = Cotizacion(cliente,[ventana])
    valor_cotizacion = cotizacion.calcular_total()
    valor_esperado = ventana.calcular_costo_total()
    assert valor_cotizacion == valor_esperado
