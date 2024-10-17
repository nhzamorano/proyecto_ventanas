import json
from cotizacion import Cotizacion
from cliente import Cliente

from database import DB

class ControladorCotizacion:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(ControladorCotizacion, cls).__new__(cls)
            cls.__instance.clientes = []
            cls.__instance.cotizaciones = []
            cls.__instance.ventanas = []
            cls.__instance.data = cls.__instance.cargar_datos()
        return cls.__instance
    
    def clear_lists(self):
        """Método para vaciar los arreglos para una nueva cotización."""
        self.clientes.clear()
        self.cotizaciones.clear()
        self.ventanas.clear()

    @classmethod
    def cargar_datos(cls):
        archivo_json = 'data.json'
        try: 
            with open(archivo_json, 'r') as archivo:
                data = json.load(archivo)
                return data 
        except FileNotFoundError:
            print(f"Elarchivo {archivo_json} no se encontro.")
            return {}
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo JSON.")
            return {}
    
    def agregar_cliente(self,nombre, empresa, cantidad_ventanas):
        self.cliente = Cliente(nombre,empresa,cantidad_ventanas)
        self.clientes.append(self.cliente)
        return self.cliente
    
    def agregar_ventanas(self,estilo, ancho, alto, acabado, tipo_vidrio, cantidad,  esmerilado):
        from ventana import Ventana
        self.ventana = Ventana(estilo, ancho, alto, acabado, tipo_vidrio, cantidad, esmerilado)
        self.ventanas.append(self.ventana)
        return self.ventana

    def crear_cotizacion(self,cliente,ventanas):
        nueva_cotizacion = Cotizacion(cliente,ventanas)
        self.cotizaciones.append(nueva_cotizacion)
        self.total = nueva_cotizacion.calcular_total()
        return nueva_cotizacion
    
    def obtener_cotizaciones(self):
        return self.cotizaciones 
    
    def obtener_clientes(self):
        return self.clientes 
    
    def obtener_ventanas(self):
        """Método que retorna la lista de ventanas."""
        return [ventana.to_list() for ventana in self.ventanas]
    

