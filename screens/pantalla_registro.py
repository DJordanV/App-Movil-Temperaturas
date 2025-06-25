import csv
import os
from pathlib import Path

from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText, MDSnackbarSupportingText
from kivy.metrics import dp
from kivy.clock import Clock

from utils.registro_temperatura import guardar_temperatura
from utils.control_camaras import cargar_nombres_camaras

CSV_CAMARAS = Path("data/app/camaras.csv")


class PantallaRegistro(MDScreen):
    def on_pre_enter(self):
        self.menu_abierto = False
        self.menu = None
        self.ids.temp_input.text = ''
        self.ids.camara_input.text = ''
        self.cargar_camaras()
    def volver_inicio(self):
        self.manager.current = 'inicio'

    def guardar_datos(self):
        camara = self.ids.camara_input.text
        temperatura_str = self.ids.temp_input.text

        if camara not in self.nombres_camaras:
            MDSnackbar(
                MDSnackbarText(
                    text="Error",
                ),
                MDSnackbarSupportingText(
                    text="El nombre de la cámara no existe",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.5,
            ).open()
            return

        try:
            temperatura = float(temperatura_str)
        except ValueError:
            MDSnackbar(
                MDSnackbarText(
                    text="Error",
                ),
                MDSnackbarSupportingText(
                    text="Temperatura no válida",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.5,
            ).open()
            return
        
        exito = guardar_temperatura(camara, temperatura)
        if exito:
            MDSnackbar(
                MDSnackbarText(
                    text="Guardado",
                ),
                MDSnackbarSupportingText(
                    text=f'{temperatura}ºC   -   {camara}',
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.5,
            ).open()
            self.ids.temp_input.text = ''
            self.ids.camara_input.text = ''
        else:
            MDSnackbar(
                MDSnackbarText(
                    text='Error',
                ),
                MDSnackbarSupportingText(
                    text='No se ha guardado el registro',
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.5,
            ).open()
    
    def abrir_menu(self, caller):
        if not os.path.exists(CSV_CAMARAS):
            MDSnackbar(
                MDSnackbarText(
                    text="Error",
                ),
                MDSnackbarSupportingText(
                    text="No se encontró el listado de cámaras",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.5,
            ).open()
            return

        items = [
            {
                'text': nombre,
                'on_release': lambda x=nombre: self.seleccionar_camara(x)
            }
            for nombre in self.nombres_camaras
        ]

        self.menu = MDDropdownMenu(
            caller=caller,
            items=items,
            border_margin=dp(24)            
        )
        self.menu.open()
    
    def seleccionar_camara(self, texto):
        self.ids.camara_input.text = texto
        self.menu.dismiss()

    def cargar_camaras(self):
        self.nombres_camaras = cargar_nombres_camaras()