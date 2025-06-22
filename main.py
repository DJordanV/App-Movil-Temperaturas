from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from screens.pantalla_inicio import PantallaInicio
from screens.pantalla_registro import PantallaRegistro

class AppTemperaturas(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        Builder.load_file('main.kv')

        sm = ScreenManager()
        sm.add_widget(PantallaInicio(name='inicio'))
        sm.add_widget(PantallaRegistro(name='registro'))

        return sm
    
if __name__ == '__main__':
    AppTemperaturas().run()