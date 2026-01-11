import os
from kivy.config import Config

# Estabilização total
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
Config.set('graphics', 'multisamples', '0')

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
        
        self.screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical', padding=30, spacing=20)

        # Título Profissional Neon
        layout.add_widget(MDLabel(
            text="SUPREME FLY PRO",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=get_color_from_hex('#39FF14'),
            bold=True
        ))

        # CARD EIXO X (Limite 1000)
        card_x = MDCard(orientation='vertical', padding=20, size_hint_y=None, height="125dp", md_bg_color=get_color_from_hex('#1A1A1A'), radius=[15,])
        self.label_x = MDLabel(text="SUAVIZAÇÃO EIXO X: 500", theme_text_color="Primary", bold=True)
        self.slider_x = MDSlider(min=1, max=1000, value=500, color_active=get_color_from_hex('#39FF14'))
        self.slider_x.bind(value=self.update_val)
        card_x.add_widget(self.label_x)
        card_x.add_widget(self.slider_x)
        layout.add_widget(card_x)

        # CARD EIXO Y (Limite 1000)
        card_y = MDCard(orientation='vertical', padding=20, size_hint_y=None, height="125dp", md_bg_color=get_color_from_hex('#1A1A1A'), radius=[15,])
        self.label_y = MDLabel(text="SUAVIZAÇÃO EIXO Y: 500", theme_text_color="Primary", bold=True)
        self.slider_y = MDSlider(min=1, max=1000, value=500, color_active=get_color_from_hex('#00E5FF'))
        self.slider_y.bind(value=self.update_val)
        card_y.add_widget(self.label_y)
        card_y.add_widget(self.slider_y)
        layout.add_widget(card_y)

        # Botão de Ativação Shizuku
        self.btn = MDFillRoundFlatIconButton(
            icon="shield-check",
            text="ATIVAR MOTOR SHIZUKU",
            pos_hint={"center_x": .5},
            size_hint_x=1,
            md_bg_color=get_color_from_hex('#1A1A1A'),
            text_color=get_color_from_hex('#39FF14')
        )
        self.btn.bind(on_release=self.conectar_shizuku)
        layout.add_widget(self.btn)

        self.screen.add_widget(layout)
        return self.screen

    def update_val(self, *args):
        self.label_x.text = f"SUAVIZAÇÃO EIXO X: {int(self.slider_x.value)}"
        self.label_y.text = f"SUAVIZAÇÃO EIXO Y: {int(self.slider_y.value)}"

    def conectar_shizuku(self, *args):
        try:
            from jnius import autoclass
            Shizuku = autoclass('moe.shizuku.api.ShizukuService')
            if Shizuku.pingBinder():
                self.btn.text = "SISTEMA OTIMIZADO ✅"
                self.btn.md_bg_color = get_color_from_hex('#39FF14')
                self.btn.text_color = [0,0,0,1]
        except Exception:
            self.btn.text = "SHIZUKU NÃO ENCONTRADO"
            self.btn.md_bg_color = [0.8, 0, 0, 1]

if __name__ == '__main__':
    SupremeFlyApp().run()
