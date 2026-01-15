import os
from kivy.config import Config
os.environ['KIVY_GL_BACKEND'] = 'sdl2'

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.screen = MDScreen()
        
        self.btn = MDFillRoundFlatIconButton(
            icon="controller", text="ATIVAR PERFORMANCE MÁXIMA",
            pos_hint={"center_x": .5, "center_y": .5},
            md_bg_color=get_color_from_hex('#39FF14')
        )
        self.btn.bind(on_release=self.turbo_boost)
        self.screen.add_widget(self.btn)
        return self.screen

    def turbo_boost(self, *args):
        try:
            # Comandos nível Scene Plus via Shizuku Shell
            os.system("cmd power set-fixed-performance-mode-enabled true")
            os.system("settings put global activity_manager_constants max_cached_processes=128")
            os.system("settings put global window_animation_scale 0.5")
            self.btn.text = "MODO TURBO: ATIVO ✅"
            self.btn.md_bg_color = [0, 0.8, 0, 1]
        except Exception as e:
            self.btn.text = "ERRO: ATIVE O SHIZUKU"

if __name__ == '__main__':
    SupremeFlyApp().run()
