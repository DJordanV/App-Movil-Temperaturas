import csv
import os
from datetime import datetime

RUTA_CSV = "data/registro_temperaturas.csv"

def guardar_temperatura(camara: str, temperatura: float) -> bool:
    """
    Guarda un registro de la temperatura validado en un CSV.
    Devuelve True si se guardó correctamente, False si hubo un error de validación.
    """

    now = datetime.now()
    fecha = now.strftime("%Y-%m-%d")
    hora = now.strftime("%H:%M")

    # Validación de tipo de cámara
    if camara not in ['Frigorífica 01', 'Frigorífica 02', 'Congelación', 'Fermentación 01', 'Fermentación 02']:
        print("⚠️ Tipo de cámara inválido.")
        return False
    
    # Validación de rango de temperatura
    if not (-40 <= temperatura <= 50):
        print("⚠️ Temperatura fuera de rango aceptable.")
        return False
    
    # Asegurar existencia del directorio
    os.makedirs(os.path.dirname(RUTA_CSV), exist_ok=True)

    # Guardar en CSV
    with open(RUTA_CSV, mode='a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        if archivo.tell() == 0:
            writer.writerow(['Fecha', 'Hora', 'Cámara', 'Temperatura'])
        writer.writerow([fecha, hora, camara, temperatura])

    print(f'✅ Registro guardado: {fecha} {hora} - {camara} - {temperatura}ºC')
    return True