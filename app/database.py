import json


DB = {
    "costo_por_cm_lineal": {
            "Pulido": 50700 / 100,
            "Lacado Brillante": 54200 / 100,
            "Lacado Mate": 53600 / 100,
            "Anodizado": 57300 / 100
        
    },
    "estilo_naves" : {
            "O": 1,
            "XO": 2,
            "OXO": 3,
            "OXXO": 4,
        },

    "costo_por_cm2" : {
            "Transparente": 8.25,
            "Bronce": 9.15,
            "Azul": 12.75
        }
}




archivo_json = 'data.json'
with open(archivo_json, 'w') as archivo:
    json.dump(DB,archivo,indent=4)


#print(f"Archivo {archivo_json} creado exitosamente")

#def consultar_dato(dato):
#    with open('data.json', 'r') as archivo:
#        data = json.load(archivo)
#
#        lac = data["costo_por_cm_lineal"][dato]
#        return lac
#lac =consultar_dato("Anodizado")
#print(f"El cosot de lacado brillante es: {consultar_dato("Anodizado")}")