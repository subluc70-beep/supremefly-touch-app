import os
from kivy.config import Config

# Travas de estabilidade para evitar Crash no Splash
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
from kivy.clock import Clock

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        
        self.screen = MDScreen()
        
        # Layout principal com scroll-feel
        main_layout = MDBoxLayout(orientation='vertical', padding=25, spacing=20)

        # Cabeçalho PRO
        main_layout.add_widget(MDLabel(
            text="SUPREME FLY PRO",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=get_color_from_hex('#39FF14'),
            bold=True,
            size_hint_y=None,
            height="60dp"
        ))

        # --- CARD DO EIXO X ---
        card_x = MDCard(orientation='vertical', padding=15, spacing=10, size_hint_y=None, height="120dp", md_bg_color=get_color_from_hex('#151515'), radius=[15,])
        self.label_x = MDLabel(text="SUAVIZAÇÃO EIXO X: 500", theme_text_color="Primary", font_style="Button", halign="left")
        self.slider_x = MDSlider(min=1, max=1000, value=500, color_active=get_color_from_hex('#39FF14'), thumb_color_active=get_color_from_hex('#39FF14'))
        self.slider_x.bind(value=self.update_labels)
        card_x.add_widget(self.label_x)
        card_x.add_widget(self.slider_x)
        main_layout.add_widget(card_x)

        # --- CARD DO EIXO Y ---
        card_y = MDCard(orientation='vertical', padding=15, spacing=10, size_hint_y=None, height="120dp", md_bg_color=get_color_from_hex('#151515'), radius=[15,])
        self.label_y = MDLabel(text="SUAVIZAÇÃO EIXO Y: 500", theme_text_color="Primary", font_style="Button", halign="left")
        self.slider_y = MDSlider(min=1, max=1000, value=500, color_active=get_color_from_hex('#00E5FF'), thumb_color_active=get_color_from_hex('#00E5FF'))
        self.slider_y.bind(value=self.update_labels)
        card_y.add_widget(self.label_y)
        card_y.add_widget(self.slider_y)
        main_layout.add_widget(card_y)

        # --- BOTÃO SHIZUKU (O que faz o app ser reconhecido) ---
        self.btn = MDFillRoundFlatIconButton(
            icon="shield-check",
            text="CONECTAR AO MOTOR SHIZUKU",
            pos_hint={"center_x": .5},
            size_hint_x=1,
            height="60dp",
            md_bg_color=get_color_from_hex('#1A1A1A'),
            text_color=get_color_from_hex('#39FF14')
        )
        self.btn.bind(on_release=self.check_shizuku_connection)
        main_layout.add_widget(self.btn)

        # Label de rodapé
        main_layout.add_widget(MDLabel(text="STATUS: AGUARDANDO PERMISSÃO", halign="center", font_style="Caption", theme_text_color="Hint"))

        self.screen.add_widget(main_layout)
        return self.screen

    def update_labels(self, *args):
        self.label_x.text = f"SUAVIZAÇÃO EIXO X: {int(self.slider_x.value)}"
        self.label_y.text = f"SUAVIZAÇÃO EIXO Y: {int(self.slider_y.value)}"

    def check_shizuku_connection(self, *args):
        try:
            from jnius import autoclass
            # Esta é a chamada que o Shizuku espera para 'acordar'
            Shizuku = autoclass('moe.shizuku.api.ShizukuService')
            if Shizuku.pingBinder():
                self.btn.text = "SHIZUKU CONECTADO ✅"
                self.btn.md_bg_color = get_color_from_hex('#39FF14')
                self.btn.text_color = [0,0,0,1]
        except:
            self.btn.text = "ERRO: SHIZUKU NÃO DETECTADO"
            self.btn.md_bg_color = [0.8, 0, 0, 1]

if __name__ == '__main__':
    SupremeFlyApp().run()
