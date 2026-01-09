import os
from kivy.config import Config

# Previne fechamentos e otimiza o gráfico
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
Config.set('graphics', 'multisamples', '0')

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.slider import MDSlider
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        
        self.screen = MDScreen()
        # Layout principal com fundo preto profundo
        layout = MDBoxLayout(orientation='vertical', padding=40, spacing=25)

        # Título Neon em Destaque
        layout.add_widget(MDLabel(
            text="SUPREME FLY PRO",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=get_color_from_hex('#39FF14'),
            bold=True
        ))

        # --- AJUSTE EIXO X ---
        self.label_x = MDLabel(
            text="SENSIBILIDADE X: 500", 
            halign="center", 
            theme_text_color="Primary",
            font_style="H6"
        )
        self.slider_x = MDSlider(
            min=1, max=1000, value=500, step=1, 
            color_active=get_color_from_hex('#39FF14'),
            thumb_color_active=get_color_from_hex('#39FF14')
        )
        self.slider_x.bind(value=self.update_val)
        
        # --- AJUSTE EIXO Y ---
        self.label_y = MDLabel(
            text="SENSIBILIDADE Y: 500", 
            halign="center", 
            theme_text_color="Primary",
            font_style="H6"
        )
        self.slider_y = MDSlider(
            min=1, max=1000, value=500, step=1, 
            color_active=get_color_from_hex('#00E5FF'),
            thumb_color_active=get_color_from_hex('#00E5FF')
        )
        self.slider_y.bind(value=self.update_val)

        # Adicionando os widgets ao layout
        layout.add_widget(self.label_x)
        layout.add_widget(self.slider_x)
        layout.add_widget(self.label_y)
        layout.add_widget(self.slider_y)

        # Botão de Ativação que chama o Shizuku
        self.btn = MDFillRoundFlatIconButton(
            icon="shield-check",
            text="VERIFICAR PERMISSÃO SHIZUKU",
            pos_hint={"center_x": .5},
            size_hint_x=0.9,
            md_bg_color=get_color_from_hex('#1A1A1A'),
            text_color=get_color_from_hex('#39FF14')
        )
        self.btn.bind(on_release=self.conectar_shizuku)
        layout.add_widget(self.btn)

        self.screen.add_widget(layout)
        return self.screen

    def update_val(self, *args):
        self.label_x.text = f"SENSIBILIDADE X: {int(self.slider_x.value)}"
        self.label_y.text = f"SENSIBILIDADE Y: {int(self.slider_y.value)}"

    def conectar_shizuku(self, *args):
        """ Esta função força o Shizuku a pedir permissão """
        try:
            from jnius import autoclass
            Shizuku = autoclass('moe.shizuku.api.ShizukuService')
            # O pingBinder() acorda o Shizuku no sistema
            if Shizuku.pingBinder():
                self.btn.text = "SHIZUKU AUTORIZADO ✅"
                self.btn.md_bg_color = get_color_from_hex('#39FF14')
                self.btn.text_color = [0, 0, 0, 1]
        except Exception:
            self.btn.text = "SHIZUKU NÃO ENCONTRADO"
            self.btn.md_bg_color = [0.8, 0, 0, 1]

if __name__ == '__main__':
    SupremeFlyApp().run()
