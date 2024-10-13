from controlador_cotizacion import ControladorCotizacion

class Ventana:
    def __init__(self, estilo, ancho, alto, acabado, tipo_vidrio, esmerilado=False):
        self.estilo = estilo
        self.ancho = ancho
        self.alto = alto
        self.acabado = acabado
        self.tipo_vidrio = tipo_vidrio
        self.esmerilado = esmerilado
        self.costo_esquinas = 4310
        self.costo_chapa = 16200
        self.costo_esmerilado = 5.20
        self.controlador = ControladorCotizacion()
    
    def calcular_ancho_naves(self):
        naves = self.controlador.data["estilo_naves"][self.estilo]
        return self.ancho / naves, naves

    def calcular_area_nave(self):
        ancho_nave, _ = self.calcular_ancho_naves()
        return (ancho_nave - 1.5) * (self.alto - 1.5)  

    def calcular_perimetro_nave(self):
        ancho_nave, _ = self.calcular_ancho_naves()
        return 2 * (ancho_nave + self.alto) - 4 * 4  

    def calcular_costo_aluminio(self):
        perimetro_total = self.calcular_perimetro_nave() * self.calcular_ancho_naves()[1]      
        return perimetro_total * self.controlador.data["costo_por_cm_lineal"][self.acabado]

    def calcular_costo_vidrio(self):
        area_total = self.calcular_area_nave() * self.calcular_ancho_naves()[1]
        costo_vidrio = area_total * self.controlador.data["costo_por_cm2"][self.tipo_vidrio]
        if self.esmerilado:
            costo_vidrio += area_total * self.costo_esmerilado
        return costo_vidrio

    def calcular_costo_esquinas(self):
        return self.costo_esquinas * 4

    def calcular_costo_chapa(self):
        if "X" in self.estilo:
            return self.costo_chapa
        return 0

    def calcular_costo_total(self):
        return self.calcular_costo_aluminio() + self.calcular_costo_vidrio() + self.calcular_costo_esquinas() + self.calcular_costo_chapa()
