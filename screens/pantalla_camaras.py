from pathlib import Path
import os

from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText, MDSnackbarSupportingText
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp

from utils.control_camaras import guardar_camara

CSV_CAMARAS = Path("data/app/camaras.csv")
TXT_TIPOS_CAMARAS = Path("data/app/tipos_camaras.txt")

class PantallaCamaras(MDScreen):
    def volver_inicio(self):
        self.manager.current = 'inicio'
    
    def guardar_camara(self):
        nombre = self.ids.nombre_camara.text.strip()
        tipo = self.ids.tipo_camara.text.strip()

        if not nombre:
            MDSnackbar(
                MDSnackbarText(
                    text="Error",
                ),
                MDSnackbarSupportingText(
                    text="Introduzca un nombre",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.5,
            ).open()
            return
        
        if not tipo:
            MDSnackbar(
                MDSnackbarText(
                    text="Error",
                ),
                MDSnackbarSupportingText(
                    text="Seleccione un tipo",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.5,
            ).open()
            return
        
        try:
            guardar_camara(nombre, tipo)
            MDSnackbar(
                MDSnackbarText(
                    text='Éxito',
                ),
                MDSnackbarSupportingText(
                    text=f'Cámara "{nombre}" guardada correctamente',
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.5,
            ).open()
            self.ids.nombre_camara.text = ''
            self.ids.tipo_camara.text = ''
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
        
        self.manager.get_screen('registro').cargar_camaras()
    
    def abrir_menu(self, caller):
        tipos_camara = open(TXT_TIPOS_CAMARAS, encoding='utf-8')
        if not os.path.exists(TXT_TIPOS_CAMARAS):
            MDSnackbar(
                MDSnackbarText(
                    text="Error",
                ),
                MDSnackbarSupportingText(
                    text="No se encontró el listado de tipos de cámaras",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.5,
            ).open()
            return

        items = [
            {
                'text': tipo,
                'on_release': lambda x=tipo: self.seleccionar_tipo_camara(x)
            }
            for tipo in tipos_camara
        ]

        self.menu = MDDropdownMenu(
            caller=caller,
            items=items,
            border_margin=dp(24)            
        )
        self.menu.open()
    
    def seleccionar_tipo_camara(self, texto):
        self.ids.tipo_camara.text = texto
        self.menu.dismiss()

