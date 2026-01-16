import os
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.utils import get_color_from_hex

# Configurações de ambiente para performance
os.environ['KIVY_GL_BACKEND'] = 'sdl2'

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        
        screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical', padding=25, spacing=10)

        # Título
        layout.add_widget(MDLabel(
            text="SUPREMEFLY: ESTABILIZADOR ADAPTATIVO",
            halign="center", font_style="H6",
            text_color=get_color_from_hex('#39FF14'), theme_text_color="Custom"
        ))

        # --- 1. MORTE DA ZONA (DEADZONE) ---
        # Ignora os primeiros milímetros para evitar que o toque inicial trema a mira
        layout.add_widget(MDLabel(text="MORTE DA ZONA (IGNORAR MICRO-TOQUES)", theme_text_color="Secondary"))
        self.deadzone = MDSlider(min=0, max=1000, value=150, color=get_color_from_hex('#39FF14'))
        layout.add_widget(self.deadzone)

        # --- 2. SUAVIZAÇÃO DE ARRASTÃO (ANTI-TREMOR) ---
        # Prioriza o movimento principal e ignora os desvios trêmulos
        layout.add_widget(MDLabel(text="ESTABILIZADOR DE INTENÇÃO (ANTI-TREMOR)", theme_text_color="Secondary"))
        self.smoothing = MDSlider(min=0, max=1000, value=850, color=get_color_from_hex('#39FF14'))
        layout.add_widget(self.smoothing)

        # --- 3. AJUSTE EIXO X (VERTICAL - CIMA/BAIXO) ---
        layout.add_widget(MDLabel(text="SENSIBILIDADE X (VERTICAL)", theme_text_color="Secondary"))
        self.sensi_v = MDSlider(min=0, max=1000, value=500, color=get_color_from_hex('#39FF14'))
        layout.add_widget(self.sensi_v)

        # --- 4. AJUSTE EIXO Y (LATERAL - LADOS) ---
        layout.add_widget(MDLabel(text="SENSIBILIDADE Y (LATERAL)", theme_text_color="Secondary"))
        self.sensi_h = MDSlider(min=0, max=1000, value=500, color=get_color_from_hex('#39FF14'))
        layout.add_widget(self.sensi_h)

        # Botão Aplicar
        from kivymd.uix.button import MDFillRoundFlatButton
        btn = MDFillRoundFlatButton(
            text="ATIVAR FILTRO DE TRAJETÓRIA",
            pos_hint={"center_x": .5},
            md_bg_color=get_color_from_hex('#39FF14'),
            text_color=[0,0,0,1], size_hint_x=0.9
        )
        btn.bind(on_release=self.apply_shizuku)
        layout.add_widget(btn)

        screen.add_widget(layout)
        return screen

    def apply_shizuku(self, *args):
        # Valores convertidos para o sistema
        dz = self.deadzone.value / 1000
        smooth = self.smoothing.value / 1000
        v_sensi = self.sensi_v.value
        h_sensi = self.sensi_h.value

        try:
            # Comandos via Shizuku para alterar a filtragem do digitalizador
            # touch.filter.level define o quão agressivo é o filtro de ruído
            os.system(f"settings put global touch.filter.level {smooth * 10}")
            # Ajusta a distância de reconhecimento do toque (Morte da zona)
            os.system(f"settings put global touch.distance.scale {dz}")
            # Garante performance máxima do processador para processar o touch
            os.system("cmd power set-fixed-performance-mode-enabled true")
            
            print(f"Suavização Ativada em {smooth}")
        except:
            print("Erro Shizuku")

if __name__ == '__main__':
    SupremeFlyApp().run()
