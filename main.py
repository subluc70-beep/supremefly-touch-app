import os
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Line, Ellipse
from kivy.clock import Clock

# Tenta importar o Shizuku via JNI (Para o Shizuku reconhecer o app)
try:
    from jnius import autoclass
    Context = autoclass('android.content.Context')
    PackageManager = autoclass('android.content.pm.PackageManager')
except:
    pass

class RedZoneCircle(MDBoxLayout):
    """Círculo Central Estilo Regedit da Foto"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0, 1, 0, 1) # Verde Neon
            self.line = Line(circle=(self.center_x, self.center_y, 80), width=2)
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.line.circle = (self.center_x, self.center_y, 80)

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        
        screen = MDScreen()
        # Fundo Preto Total para destacar o Verde
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=15)

        # Cabeçalho Estilizado
        layout.add_widget(MDLabel(
            text="SUPREMEFLY V3 - REGEDIT PRO",
            halign="center", font_style="H4", 
            text_color=get_color_from_hex('#39FF14'), theme_text_color="Custom"
        ))

        # Círculo Central da Interface (Foto)
        self.circle_zone = RedZoneCircle(size_hint_y=0.3)
        layout.add_widget(self.circle_zone)

        # --- SLIDERS X e Y (0 a 1000) ---
        layout.add_widget(MDLabel(text="SENSIBILIDADE X (VERTICAL)", theme_text_color="Secondary"))
        self.sensi_x = MDSlider(min=0, max=1000, value=500, color=get_color_from_hex('#39FF14'))
        layout.add_widget(self.sensi_x)

        layout.add_widget(MDLabel(text="SENSIBILIDADE Y (LATERAL)", theme_text_color="Secondary"))
        self.sensi_y = MDSlider(min=0, max=1000, value=500, color=get_color_from_hex('#39FF14'))
        layout.add_widget(self.sensi_y)

        # --- PRIORIDADE DE ARRASTÃO (AGORA LIGAR/DESLIGAR) ---
        prio_layout = MDBoxLayout(orientation='horizontal', size_hint_y=None, height="50dp")
        prio_layout.add_widget(MDLabel(text="PRIORIDADE DE ARRASTÃO NATIVA", theme_text_color="Primary"))
        self.prio_switch = MDSwitch(active=True)
        prio_layout.add_widget(self.prio_switch)
        layout.add_widget(prio_layout)

        # --- AUTO-RESET ---
        reset_layout = MDBoxLayout(orientation='horizontal', size_hint_y=None, height="50dp")
        reset_layout.add_widget(MDLabel(text="AUTO-RESET (SAIR DO JOGO)", theme_text_color="Primary"))
        self.reset_switch = MDSwitch(active=True)
        reset_layout.add_widget(self.reset_switch)
        layout.add_widget(reset_layout)

        # Botão de Injeção
        self.btn = MDFillRoundFlatButton(
            text="INJETAR NO HARDWARE",
            pos_hint={"center_x": .5}, size_hint_x=0.9,
            md_bg_color=get_color_from_hex('#39FF14'),
            text_color=[0,0,0,1]
        )
        self.btn.bind(on_release=self.apply_hardware_logic)
        layout.add_widget(self.btn)

        # Console de Log (Blindagem)
        self.log = MDLabel(text="> Aguardando Shizuku...", font_style="Caption", theme_text_color="Hint")
        layout.add_widget(self.log)

        screen.add_widget(layout)
        return screen

    def apply_hardware_logic(self, *args):
        # Para o Shizuku reconhecer, precisamos forçar uma chamada de sistema via shell rish
        x = self.sensi_x.value / 1000
        y = self.sensi_y.value / 1000
        prio_val = 1.0 if self.prio_switch.active else 0.0

        try:
            # Comandos via rish (O binário que o Shizuku usa para dar autoridade ao app)
            os.system(f"/data/local/tmp/rish -c 'settings put global touch.pressure.scale {x}'")
            os.system(f"/data/local/tmp/rish -c 'settings put global touch.size.scale {y}'")
            os.system(f"/data/local/tmp/rish -c 'settings put global touch.filter.abscenter {prio_val}'")
            
            self.log.text = f"> INJETADO: X={x} Y={y} PRIO={prio_val}"
            self.btn.text = "SISTEMA OTIMIZADO ✅"
        except Exception as e:
            self.log.text = f"> ERRO: {str(e)}"

if __name__ == '__main__':
    SupremeFlyApp().run()
