import os
from kivy.config import Config

# Ajustes de estabilidade para evitar fechamento em Androids específicos
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'multisamples', '0')

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.slider import MDSlider
from kivymd.uix.button import MDRoundFlatIconButton
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        Window.clearcolor = get_color_from_hex('#0A0A0A')
        
        self.screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical', padding=30, spacing=20)

        # Título Neon
        layout.add_widget(MDLabel(
            text="SUPREME FLY PRO",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=get_color_from_hex('#39FF14')
        ))

        # --- EIXO X ---
        layout.add_widget(MDLabel(text="SENSIBILIDADE HORIZONTAL (X)", halign="center", theme_text_color="Hint"))
        self.label_x = MDLabel(text="0.5 mm", halign="center", font_style="H5")
        self.slider_x = MDSlider(min=0.1, max=1.0, value=0.5, step=0.1, color=get_color_from_hex('#39FF14'))
        self.slider_x.bind(value=self.update_x)
        layout.add_widget(self.label_x)
        layout.add_widget(self.slider_x)

        # --- EIXO Y ---
        layout.add_widget(MDLabel(text="SENSIBILIDADE VERTICAL (Y)", halign="center", theme_text_color="Hint"))
        self.label_y = MDLabel(text="0.5 mm", halign="center", font_style="H5")
        self.slider_y = MDSlider(min=0.1, max=1.0, value=0.5, step=0.1, color=get_color_from_hex('#00E5FF'))
        self.slider_y.bind(value=self.update_y)
        layout.add_widget(self.label_y)
        layout.add_widget(self.slider_y)

        # --- BOTÃO DE CALIBRAÇÃO (SHIZUKU INTERFACE) ---
        self.btn_calibrar = MDRoundFlatIconButton(
            icon="target",
            text="CALIBRAR COM SHIZUKU",
            pos_hint={"center_x": .5},
            text_color=get_color_from_hex('#FFFFFF'),
            line_color=get_color_from_hex('#39FF14'),
            size_hint_x=0.9
        )
        self.btn_calibrar.bind(on_press=self.iniciar_calibracao)
        layout.add_widget(self.btn_calibrar)

        self.screen.add_widget(layout)
        return self.screen

    def update_x(self, instance, value):
        self.label_x.text = f"{value:.1f} mm"

    def update_y(self, instance, value):
        self.label_y.text = f"{value:.1f} mm"

    def iniciar_calibracao(self, instance):
        instance.text = "CALIBRANDO VIA SHIZUKU..."
        # Simula a resposta do sistema
        Clock.schedule_once(self.finalizar_calibracao, 2.5)

    def finalizar_calibracao(self, dt):
        self.btn_calibrar.text = "CALIBRADO E OTIMIZADO!"
        self.btn_calibrar.icon = "check-decagram"

if __name__ == '__main__':
    SupremeFlyApp().run()
