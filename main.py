import os
import subprocess
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.button import MDFillRoundFlatButton, MDIconButton
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.shizuku_ready = False
        
        screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=10)

        # --- STATUS DE CONEXÃO (BLINDAGEM) ---
        self.status_bar = MDBoxLayout(size_hint_y=None, height="40dp", spacing=10)
        self.status_icon = MDIconButton(icon="shield-alert", theme_text_color="Custom", text_color=[1,0,0,1])
        self.status_text = MDLabel(text="SHIZUKU: DESCONECTADO", theme_text_color="Secondary", font_style="Caption")
        self.status_bar.add_widget(self.status_icon)
        self.status_bar.add_widget(self.status_text)
        layout.add_widget(self.status_bar)

        # --- SLIDERS (X/Y E PRIORIDADE) ---
        layout.add_widget(MDLabel(text="SENSIBILIDADE X (VERTICAL)", theme_text_color="Secondary"))
        self.sensi_x = MDSlider(min=0, max=1000, value=500, color=get_color_from_hex('#39FF14'))
        layout.add_widget(self.sensi_x)

        layout.add_widget(MDLabel(text="SENSIBILIDADE Y (LATERAL)", theme_text_color="Secondary"))
        self.sensi_y = MDSlider(min=0, max=1000, value=500, color=get_color_from_hex('#39FF14'))
        layout.add_widget(self.sensi_y)

        layout.add_widget(MDLabel(text="PRIORIDADE DE ARRASTÃO (SMOOTHING)", theme_text_color="Secondary"))
        self.priority = MDSlider(min=0, max=1000, value=800, color=get_color_from_hex('#39FF14'))
        layout.add_widget(self.priority)

        # --- AUTO-RESET ---
        reset_box = MDBoxLayout(orientation='horizontal', size_hint_y=None, height="40dp")
        reset_box.add_widget(MDLabel(text="AUTO-RESET (Sair do Jogo)"))
        self.auto_reset = MDSwitch()
        reset_box.add_widget(self.auto_reset)
        layout.add_widget(reset_box)

        # --- BOTÃO DE INJEÇÃO ---
        self.btn_apply = MDFillRoundFlatButton(
            text="INJETAR NO HARDWARE",
            pos_hint={"center_x": .5}, size_hint_x=0.9,
            md_bg_color=get_color_from_hex('#333333'), # Cinza enquanto inativo
            text_color=[1,1,1,1]
        )
        self.btn_apply.bind(on_release=self.apply_safe)
        layout.add_widget(self.btn_apply)

        # Inicia verificação de conexão
        Clock.schedule_interval(self.check_shizuku, 3)
        
        screen.add_widget(layout)
        return screen

    def check_shizuku(self, dt):
        """Verifica se o serviço Shizuku está acessível via ADB Shell"""
        try:
            # Tenta um comando simples que só funciona via Shizuku/ADB
            result = subprocess.run(['sh', '-c', 'shizuku_session echo 1'], capture_output=True, text=True)
            if "1" in result.stdout:
                self.shizuku_ready = True
                self.status_text.text = "SHIZUKU: PRONTO PARA INJEÇÃO"
                self.status_icon.icon = "shield-check"
                self.status_icon.text_color = [0,1,0,1]
                self.btn_apply.md_bg_color = get_color_from_hex('#39FF14')
                self.btn_apply.text_color = [0,0,0,1]
        except:
            self.shizuku_ready = False

    def run_shizuku_cmd(self, cmd):
        """Método blindado para enviar comandos via Shizuku"""
        # A sintaxe real para Shizuku via Python requer 'rish' ou redirecionamento de shell
        full_cmd = f"shizuku_session {cmd}"
        os.system(full_cmd)

    def apply_safe(self, *args):
        if not self.shizuku_ready:
            self.status_text.text = "ERRO: ABRA O APP SHIZUKU PRIMEIRO!"
            return

        # Captura valores
        prio = self.priority.value / 1000
        x_val = self.sensi_x.value / 1000
        y_val = self.sensi_y.value / 1000

        # Injeção Nativa Blindada
        self.run_shizuku_cmd(f"settings put global touch.filter.abscenter {prio}")
        self.run_shizuku_cmd(f"settings put global touch.pressure.scale {x_val}")
        self.run_shizuku_cmd(f"settings put global touch.size.scale {y_val}")
        self.run_shizuku_cmd("cmd power set-fixed-performance-mode-enabled true")
        
        self.btn_apply.text = "SISTEMA BLINDADO ✅"

if __name__ == '__main__':
    SupremeFlyApp().run()
