import os
from kivy.config import Config
os.environ['KIVY_GL_BACKEND'] = 'sdl2'

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.slider import MDSlider
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.card import MDCard
from kivy.utils import get_color_from_hex

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        layout = MDBoxLayout(orientation='vertical', padding=30, spacing=20)

        layout.add_widget(MDLabel(
            text="SUPREME FLY TURBO", halign="center", font_style="H4",
            theme_text_color="Custom", text_color=get_color_from_hex('#39FF14'), bold=True
        ))

        # Sliders de Suavização (Simulando Scene 2)
        for eixo in ["X", "Y"]:
            card = MDCard(orientation='vertical', padding=20, size_hint_y=None, height="120dp", md_bg_color=get_color_from_hex('#1A1A1A'))
            label = MDLabel(text=f"SUAVIZAÇÃO {eixo}: 500", theme_text_color="Primary")
            slider = MDSlider(min=1, max=1000, value=500, color_active=get_color_from_hex('#39FF14'))
            card.add_widget(label)
            card.add_widget(slider)
            layout.add_widget(card)

        self.btn = MDFillRoundFlatIconButton(
            icon="flash", text="ATIVAR OTIMIZAÇÃO SCENE",
            pos_hint={"center_x": .5}, size_hint_x=1,
            md_bg_color=get_color_from_hex('#39FF14'), text_color=[0,0,0,1]
        )
        self.btn.bind(on_release=self.ativar_turbo)
        layout.add_widget(self.btn)

        self.screen = MDScreen()
        self.screen.add_widget(layout)
        return self.screen

    def ativar_turbo(self, *args):
        # Executa comandos de performance via Shell (Funciona com Shizuku ativo)
        try:
            os.system("settings put global power_manager_constants power_save_disabled=true")
            os.system("cmd power set-fixed-performance-mode-enabled true")
            self.btn.text = "MODO PERFORMANCE ATIVO ✅"
            self.btn.md_bg_color = [0, 1, 0, 1]
        except:
            self.btn.text = "ERRO NA ATIVAÇÃO"

if __name__ == '__main__':
    SupremeFlyApp().run()
