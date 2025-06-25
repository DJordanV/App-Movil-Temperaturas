import csv
import os
from pathlib import Path

CSV_CAMARAS = Path("data/app/camaras.csv")

os.makedirs(os.path.dirname(CSV_CAMARAS), exist_ok=True)

def guardar_camara(nombre, tipo):
    camaras = cargar_camaras()
    if any(c['Nombre'] == nombre for c in camaras):
        raise ValueError('Ya existe una cámara con ese nombre.')
    with open(CSV_CAMARAS, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Nombre', 'Tipo'])
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow({'Nombre': nombre, 'Tipo': tipo})

def cargar_camaras():
    if not CSV_CAMARAS.exists():
        return[]
    with open(CSV_CAMARAS, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)