from pathlib import Path
import os

from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText, MDSnackbarSupportingText
from kivy.metrics import dp

TXT_TIPOS_CAMARAS = Path("data/app/tipos_camaras.txt")
os.makedirs(os.path.dirname(TXT_TIPOS_CAMARAS), exist_ok=True)

class PantallaNuevoTipoCamara(MDScreen):
    def volver_camaras(self):
        self.manager.current = 'camaras'

    def guardar_tipo_camara(self):
        nuevo_tipo = self.ids.nuevo_tipo_camara.text.strip()
        tipos_camara = open(TXT_TIPOS_CAMARAS, encoding='utf-8')

        if not nuevo_tipo:
            MDSnackbar(
                MDSnackbarText(
                    text="Error",
                ),
                MDSnackbarSupportingText(
                    text="Introduzca un nuevo tipo de cámara",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.5,
            ).open()
            return
        
        if nuevo_tipo in tipos_camara:
            MDSnackbar(
                MDSnackbarText(
                    text="Error",
                ),
                MDSnackbarSupportingText(
                    text="El tipo introducido ya existe",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.5,
            ).open()
            return
        
        try:
            with open(TXT_TIPOS_CAMARAS, mode='a', encoding='utf-8') as f:
                f.write(f'\n{nuevo_tipo}')
            MDSnackbar(
                MDSnackbarText(
                    text=nuevo_tipo,
                ),
                MDSnackbarSupportingText(
                    text='Nuevo tipo de cámara guardado con éxito'
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.5,
            ).open()
            self.ids.nuevo_tipo_camara.text = ''
        except ValueError as e:
            MDSnackbar(
                MDSnackbarText(
                    text="Error",
                ),
                MDSnackbarSupportingText(
                    text=str(e)
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.5,
            ).open()