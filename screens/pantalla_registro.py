from kivymd.uix.screen import MDScreen

class PantallaRegistro(MDScreen):
    def volver_inicio(self):
        self.manager.current = 'inicio'