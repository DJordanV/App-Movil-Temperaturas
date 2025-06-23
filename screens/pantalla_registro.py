from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp
from kivy.clock import Clock
from utils.registro_temperatura import guardar_temperatura

class PantallaRegistro(MDScreen):
    def on_pre_enter(self):
        self.ids.temp_input.text = ''
        self.ids.camara_field.text = ''

    def volver_inicio(self):
        self.manager.current = 'inicio'

    def guardar_datos(self):
        camara = self.ids.camara_field.text
        temperatura_str = self.ids.temp_input.text

        if camara not in ['Frigorífica 01', 'Frigorífica 02', 'Congelación', 'Fermentación 01', 'Fermentación 02']:
            self.mostrar_dialogo('⚠️ Selecciona una cámara.')

        try:
            temperatura = float(temperatura_str)
        except ValueError:
            self.mostrar_dialogo('⚠️ Temperatura no válida.')
            return
        
        exito = guardar_temperatura(camara, temperatura)
        if exito:
            self.mostrar_dialogo('✅ Registro guardado con éxito.')
            self.ids.temp_input.text = ''
            self.ids.camara_field.text = ''
        else:
            self.mostrar_dialogo('❌ Error al guardar el registro.')
    
    def mostrar_dialogo(self, mensaje):
        dialogo = MDDialog(text=mensaje, size_hint=(0.8, 0.3))
        dialogo.open()

    def abrir_menu(self, caller):
        items= [
            {"viewclass": "OneLineListItem", "text": "Frigorífica 01", "on_release": lambda x="Frigorífica 01": self.seleccionar_camara(x)},
            {"viewclass": "OneLineListItem", "text": "Frigorífica 02", "on_release": lambda x="Frigorífica 02": self.seleccionar_camara(x)},
            {"viewclass": "OneLineListItem", "text": "Congelación", "on_release": lambda x="Congelación": self.seleccionar_camara(x)},
            {"viewclass": "OneLineListItem", "text": "Fermentación 01", "on_release": lambda x="Fermentación 01": self.seleccionar_camara(x)},
            {"viewclass": "OneLineListItem", "text": "Fermentación 02", "on_release": lambda x="Fermentación 02": self.seleccionar_camara(x)},
        ]
        self.menu = MDDropdownMenu(
            caller = caller,
            items = items,
            width_mult = 4
        )
        self.menu.open()
    
    def seleccionar_camara(self, texto):
        self.ids.camara_field.text = texto
        self.menu.dismiss()