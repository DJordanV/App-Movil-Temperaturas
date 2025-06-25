from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from screens.pantalla_inicio import PantallaInicio
from screens.pantalla_registro import PantallaRegistro
from screens.pantalla_camaras import PantallaCamaras
from screens.pantalla_nuevo_tipo_camara import PantallaNuevoTipoCamara

class AppTemperaturas(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.primary_hue = '500'
        
        Builder.load_file('main.kv')

        sm = ScreenManager()
        sm.add_widget(PantallaInicio(name='inicio'))
        sm.add_widget(PantallaRegistro(name='registro'))
        sm.add_widget(PantallaCamaras(name='camaras'))
        sm.add_widget(PantallaNuevoTipoCamara(name='nuevo_tipo_camara'))

        return sm
    
if __name__ == '__main__':
    AppTemperaturas().run()