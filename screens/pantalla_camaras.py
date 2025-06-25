from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText, MDSnackbarSupportingText
from kivy.metrics import dp

from utils.control_camaras import guardar_camara

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

