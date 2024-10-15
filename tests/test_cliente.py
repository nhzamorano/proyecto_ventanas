import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.cliente import Cliente

def test_create_cliente():
    cliente = Cliente("Juan Perez","Aceros ZZ",10)
    assert cliente.nombre == "Juan Perez"
    assert cliente.empresa == "Aceros ZZ"
    assert cliente.cantidad_ventanas == 10
