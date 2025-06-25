import csv
import os
from datetime import datetime
from pathlib import Path

CSV_REGISTROS = "data/registros/registro_temperaturas.csv"
CSV_CAMARAS = Path("data/app/camaras.csv")

def guardar_temperatura(camara: str, temperatura: float) -> bool:
    """
    Guarda un registro de la temperatura validado en un CSV.
    Devuelve True si se guardó correctamente, False si hubo un error de validación.
    """

    now = datetime.now()
    fecha = now.strftime("%Y-%m-%d")
    hora = now.strftime("%H:%M")

    with open(CSV_CAMARAS, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        camaras_dict = {row['Nombre']: row['Tipo'] for row in reader}
        nombres_camaras = list(camaras_dict.keys())
        

    # Validación de tipo de cámara
    if camara not in nombres_camaras:
        print("⚠️ Tipo de cámara inválido.")
        return False
    
    # Validación de rango de temperatura
    if not (-40 <= temperatura <= 50):
        print("⚠️ Temperatura fuera de rango aceptable.")
        return False
    
    # Recoge el tipo de cámara asociado al nombre
    tipo_camara = camaras_dict[camara]
    
    # Asegurar existencia del directorio
    os.makedirs(os.path.dirname(CSV_REGISTROS), exist_ok=True)

    # Guardar en CSV
    with open(CSV_REGISTROS, mode='a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        if archivo.tell() == 0:
            writer.writerow(['Fecha', 'Hora', 'Camara', 'Temperatura', 'TipoCamara'])
        writer.writerow([fecha, hora, camara, temperatura, tipo_camara])

    print(f'✅ Registro guardado: {fecha} {hora} - {camara} - {temperatura}ºC')
    return True