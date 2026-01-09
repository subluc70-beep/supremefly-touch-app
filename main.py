import os
from kivy.config import Config

# Força o uso do motor gráfico SDL2 (evita fechar em celulares novos)
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
        layout = MDBoxLayout(orientation='vertical', padding=40, spacing=25)

        # Título Neon
        layout.add_widget(MDLabel(
            text="SUPREME FLY PRO",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=get_color_from_hex('#39FF14'),
            bold=True
        ))

        # --- EIXO X (1 a 1000) ---
        self.label_x = MDLabel(text="SENSIBILIDADE X: 500", halign="center")
        self.slider_x = MDSlider(min=1, max=1000, value=500, color_active=get_color_from_hex('#39FF14'))
        self.slider_x.bind(value=self.update_val)
        
        # --- EIXO Y (1 a 1000) ---
        self.label_y = MDLabel(text="SENSIBILIDADE Y: 500", halign="center")
        self.slider_y = MDSlider(min=1, max=1000, value=500, color_active=get_color_from_hex('#00E5FF'))
        self.slider_y.bind(value=self.update_val)

        layout.add_widget(self.label_x)
        layout.add_widget(self.slider_x)
        layout.add_widget(self.label_y)
        layout.add_widget(self.slider_y)

        # Botão de Ativação
        self.btn = MDFillRoundFlatIconButton(
            icon="shield-check",
            text="CONECTAR AO SHIZUKU",
            pos_hint={"center_x": .5},
            size_hint_x=0.9
        )
        self.btn.bind(on_release=self.conectar_shizuku)
        layout.add_widget(self.btn)

        self.screen.add_widget(layout)
        return self.screen

    def update_val(self, *args):
        self.label_x.text = f"SENSIBILIDADE X: {int(self.slider_x.value)}"
        self.label_y.text = f"SENSIBILIDADE Y: {int(self.slider_y.value)}"

    def conectar_shizuku(self, *args):
        # O truque está aqui: só importa a jnius quando clica, 
        # para o app não dar erro se ela não carregar rápido
        try:
            from jnius import autoclass
            Shizuku = autoclass('moe.shizuku.api.ShizukuService')
            if Shizuku.pingBinder():
                self.btn.text = "SHIZUKU ATIVO ✅"
                self.btn.md_bg_color = get_color_from_hex('#39FF14')
        except:
            self.btn.text = "ABRA O APP SHIZUKU"
            self.btn.md_bg_color = [1, 0, 0, 1]

if __name__ == '__main__':
    SupremeFlyApp().run()
