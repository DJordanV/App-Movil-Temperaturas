from kivymd.uix.screen import MDScreen

class PantallaInicio(MDScreen):
    def ir_a_registro(self):
        self.manager.current = 'registro'