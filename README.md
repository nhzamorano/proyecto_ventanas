# Sistema de Cotización de Ventanas para la Compañía PQR
Proyecto Cotizacion Ventanas
## Descripción

Este proyecto consiste en el desarrollo de un sistema de cotización de ventanas 
para la empresa PQR, con el fin de automatizar su proceso manual. El sistema 
permite calcular el costo total de las ventanas basándose en el estilo de la ventana, 
tipo de vidrio, acabado de aluminio y otros componentes adicionales.

## Características
- Cálculo de costos para diferentes estilos de ventanas (O, XO, OXXO, OXO).
- Tipos de vidrios y acabados de aluminio.
- Inclusión de componentes adicionales como esquinas y chapas.
- Aplicación de descuentos para pedidos superiores a 100 ventanas.
- Generación de cotización detallada.

# Intalacion
Pudes clonar el proyecto desde github
git clone https://github.com/nhzamorano/proyecto_ventanas.git
Instala las dependencias desde el archivo requirements.txt
pip install -r requirements.txt

# Ejecucion
El programa cuenta con dos interfaces de ejecucion, una es tipo caracter, la otra es interfaz web usando el framework Flask.
- Para ejecutar la instancia tipo caracter hacerlo de la manera sicuiente: python app\main.py
- Para ejecutar la instancia por interfaz web hacerlo de la manera siguiente: python app\index.py, se carga por el puerto 8000, del    localhost o de la direccion ip que la red asigne.


# Cualidades
Se implemento a travez de un patron singlenton el cual administra toda la aplicacion y maneja la conexion y carga de los datos desde un archivo json.


# Futuras mejoras
Se podrian incluir en lugar de un archivo json una base de datos donde se almacenen los datos basicos de las dimensiones y tipos de ventanas, adicionalmente incluir tablas que manejen los clientes y el movimiento de las cotizaciones que estos clientes generen.

# Licencia
GNU General Public License (GPL)
Link: https://www.gnu.org/licenses/gpl-3.0.html

# Tecnologias utilizadas
- Python
- Flask 
- Rich
- Json
- Bootstrap 5

## Contribuir
¡Las contribuciones, mejoras, correcciones y sugerencias son bienvenidas!

Si deseas ayudar a mejorar este proyecto, sigue estos pasos:
1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commits.
4. Abre un pull request para que podamos revisarlo.

Si tienes ideas, problemas o preguntas, no dudes en abrir un issue. ¡Toda ayuda es apreciada!

