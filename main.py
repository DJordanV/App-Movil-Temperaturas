from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(orientation='vertical', padding=40, spacing=20)

        label = MDLabel(
            text='Bienvenido a la App de Registro de Temperaturas',
            halign= 'center',
            theme_text_color= 'Primary',
            font_style='H5'
        )

        button = MDRaisedButton(
            text='Registrar Temperatura',
            pos_hint={'center_x': 0.5},
            on_release=self.on_register
        )

        layout.add_widget(label)
        layout.add_widget(button)

        self.add_widget(layout)
    
    def on_register(self, instance):
        print('Botón pulsado - Aquí irá el registro')

class AppTemperaturas(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'BlueGray'
        return MainScreen()

if __name__ == '__main__':
    AppTemperaturas().run()