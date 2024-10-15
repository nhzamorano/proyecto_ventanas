class Cotizacion:
    def __init__(self, cliente, ventanas):
        self.cliente = cliente
        self.ventanas = ventanas
        self.porcentaje = 0.1
        self.porcengtaje_iva = 0.19 

    def calcular_total(self):
        costo_unitario = sum(ventana.calcular_costo_total() for ventana in self.ventanas)
        costo_bruto = int(costo_unitario) * int(self.cliente.cantidad_ventanas)
        descuento = 0
        #costo_bruto = sub_total
        #iva = costo_bruto*self.porcengtaje_iva
        if int(self.cliente.cantidad_ventanas) > 100:
            descuento = int(costo_bruto) * self.porcentaje
            #total = costo_bruto - descuento
        return costo_bruto,descuento
