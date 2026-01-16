import os
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.utils import get_color_from_hex

# Forçamos a aceleração de hardware para evitar a tela preta
os.environ['KIVY_GL_BACKEND'] = 'sdl2'

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        
        # Layout Principal para evitar que apareça só um botão perdido
        layout = MDBoxLayout(orientation='vertical', padding=40, spacing=20)
        
        # Título do App
        layout.add_widget(MDLabel(
            text="SUPREME FLY PRO",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=get_color_from_hex('#39FF14')
        ))

        # Botão de Ativação
        self.btn = MDFillRoundFlatIconButton(
            icon="flash",
            text="ATIVAR MODO TURBO (SHIZUKU)",
            pos_hint={"center_x": .5},
            size_hint_x=0.9,
            md_bg_color=get_color_from_hex('#39FF14'),
            text_color=[0, 0, 0, 1]
        )
        self.btn.bind(on_release=self.run_shizuku_commands)
        layout.add_widget(self.btn)

        # Status Label
        self.status = MDLabel(
            text="Status: Aguardando Ativação",
            halign="center",
            theme_text_color="Secondary"
        )
        layout.add_widget(self.status)

        screen = MDScreen()
        screen.add_widget(layout)
        return screen

    def run_shizuku_commands(self, *args):
        # Aqui o app tenta se comunicar com o Shizuku via Shell
        try:
            # Comando 1: Força o modo de performance máxima
            os.system("sh /sdcard/shizuku_shell.sh -c 'cmd power set-fixed-performance-mode-enabled true'")
            # Comando 2: Otimiza a resposta do toque
            os.system("settings put global touch_acceleration_enabled 1")
            
            self.status.text = "Status: PERFORMANCE ATIVADA! ✅"
            self.status.theme_text_color = "Primary"
            self.btn.text = "OTIMIZADO"
            self.btn.disabled = True
        except Exception as e:
            self.status.text = "Erro: Certifique-se que o Shizuku está iniciado."

if __name__ == '__main__':
    SupremeFlyApp().run()
