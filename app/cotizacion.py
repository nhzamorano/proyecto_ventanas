class Cotizacion:
    def __init__(self, cliente, ventanas):
        self.cliente = cliente
        self.ventanas = ventanas
        self.porcentaje = 0.9
        self.porcengtaje_iva = 0.19 

    def calcular_total(self):
        total = sum(ventana.calcular_costo_total() for ventana in self.ventanas)
        descuento = 0
        costo_bruto = total
        #iva = costo_bruto*self.porcengtaje_iva
        if self.cliente.cantidad_ventanas > 100:
            total *= self.porcentaje  # Apply 10% discount
            descuento = costo_bruto - total
        return total,descuento,costo_bruto
