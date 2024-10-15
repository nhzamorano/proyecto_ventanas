import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ..app.ventana import Ventana

def test_create_ventana():
    ventana = Ventana('XO',15,20,'Pulido','Azul',True)
    assert ventana.estilo == 'XO'
    assert ventana.ancho == 15
    assert ventana.alto == 20
    assert ventana.acabado == 'Pulido'
    assert ventana.tipo_vidrio == 'Azul'
    assert ventana.esmerilado == True 

def test_calcular_ancho_naves():
    ventana = Ventana('OXO',15,20,'Pulido','Azul',True)
    ancho_por_nave, naves = ventana.calcular_ancho_naves()
    assert ancho_por_nave == 5
    assert naves == 3

def test_calcular_area_nave():
    ventana = Ventana('OXO',15,20,'Pulido','Azul',True)
    area_nave = ventana.calcular_area_nave()
    # Para 'OXO', el ancho por nave es 5.0 (15/3), el area seria:
    # (5.0 - 1.5) * (20 - 1.5) = 3.5 * 18.5 = 64.75
    assert area_nave == 64.75

def test_calcualar_perimetro_nave():
    ventana = Ventana('OXO',15,20,'Pulido','Azul',True)
    perimetro_nave = ventana.calcular_perimetro_nave()
    # Para 'OXO', el ancho por nave es 5.0 (15/3), el perimetro seria:
    # 2 * (5.0 + 20) - 16 = 2 * 25 - 16 = 50 - 16 = 34
    assert perimetro_nave == 34

def test_calcular_costo_aluminio():
    ventana = Ventana('OXO',15,20,'Pulido','Azul',True)
    perimetro_nave = ventana.calcular_perimetro_nave()
    naves = ventana.calcular_ancho_naves()[1]
    costo_cm_lineal = 50700 / 100
    perimetro_total = perimetro_nave * naves 
    costo_total = perimetro_total * costo_cm_lineal
    assert ventana.calcular_costo_aluminio() == costo_total

def test_calcular_costo_vidrio():
    ventana = Ventana('OXO',15,20,'Pulido','Azul',True)
    ventana.tipo_vidrio = 'Azul'
    area_nave = ventana.calcular_area_nave()
    naves = ventana.calcular_ancho_naves()[1]
    costo_por_cm2 = 12.75
    # 64.75 * 3 = 194.25
    area_total = area_nave * naves
    # 194.25 * 12.75 = 2473.6875
    costo_vidrio = area_total * costo_por_cm2
    if ventana.esmerilado:
         # 194.25 * 5.20 = 1017.3
        costo_vidrio += area_total * 5.20
    costo_total = costo_vidrio
    assert ventana.calcular_costo_vidrio() == costo_total

def test_calcular_costo_esquinas():
    ventana = Ventana('OXO',15,20,'Pulido','Azul',True)
    costo_esquinas = ventana.calcular_costo_esquinas()
    assert costo_esquinas == 17240

def test_calcular_chapa():
    ventana = Ventana('OXO',15,20,'Pulido','Azul',True)
    assert ventana.calcular_costo_chapa() == 16200

def test_calcular_costo_total():
    ventana = Ventana('OXO',15,20,'Pulido','Azul',True)
    costo_aluminio = ventana.calcular_costo_aluminio()
    costo_vidrio = ventana.calcular_costo_vidrio()
    costo_esquinas = ventana.calcular_costo_esquinas()
    costo_chapa = ventana.calcular_costo_chapa()
    costo_total = costo_aluminio+costo_vidrio+costo_esquinas+costo_chapa
    assert costo_total == 88640.7875

    