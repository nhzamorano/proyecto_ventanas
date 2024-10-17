class Cotizacion:
    def __init__(self, cliente, ventanas):
        self.cliente = cliente
        self.ventanas = ventanas
        self.porcentaje = 0.1
        self.porcengtaje_iva = 0.19 

    def calcular_total(self):
        costo_unitario = sum(ventana.calcular_costo_total() for ventana in self.ventanas)
        costo_bruto = float(costo_unitario) 
        descuento = 0
        if int(self.cliente.cantidad_ventanas) > 100:
            descuento = float(costo_bruto) * self.porcentaje
        return costo_bruto,float(descuento)
