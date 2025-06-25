import csv
import os
from pathlib import Path

CSV_CAMARAS = Path("data/app/camaras.csv")

os.makedirs(os.path.dirname(CSV_CAMARAS), exist_ok=True)

def guardar_camara(nombre, tipo):
    nombres_camaras = cargar_nombres_camaras()
    if any(n == nombre for n in nombres_camaras):
        raise ValueError('Ya existe una cámara con ese nombre.')
    with open(CSV_CAMARAS, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Nombre', 'Tipo'])
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow({'Nombre': nombre, 'Tipo': tipo})

def cargar_nombres_camaras():
    if not CSV_CAMARAS.exists():
        return[]
    with open(CSV_CAMARAS, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        nombres_camaras = [row[0] for row in reader] 
        return nombres_camaras

def cargar_camaras_dict_tipo():
    if not CSV_CAMARAS.exists():
        return{}
    with open(CSV_CAMARAS, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        camaras_dict = {row['Nombre']: row['Tipo'] for row in reader}
        return camaras_dict