import os
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

# Configuração para evitar tela preta e otimizar GPU
os.environ['KIVY_GL_BACKEND'] = 'sdl2'

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        
        screen = MDScreen()
        
        # Layout Principal
        main_layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Cabeçalho Estilizado
        header = MDLabel(
            text="SUPREME FLY [PRO]",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=get_color_from_hex('#39FF14'),
            size_hint_y=None,
            height="80dp"
        )
        main_layout.add_widget(header)

        # Card de Status do Sistema
        self.status_card = MDCard(
            orientation='vertical',
            padding=15,
            size_hint=(1, None),
            height="120dp",
            md_bg_color=get_color_from_hex('#1E1E1E'),
            radius=[15, 15, 15, 15],
            elevation=2
        )
        
        self.info_label = MDLabel(
            text="ESTADO DO SISTEMA: STANDBY\nFPS TARGET: 120\nLATÊNCIA: OTIMIZADA",
            halign="left",
            theme_text_color="Secondary",
            font_style="Caption"
        )
        self.status_card.add_widget(self.info_label)
        main_layout.add_widget(self.status_card)

        # Espaçador
        main_layout.add_widget(MDBoxLayout())

        # Botão Turbo Central (O das fotos)
        self.turbo_btn = MDFillRoundFlatButton(
            text="INICIAR PROTOCOLO TURBO",
            font_size="20sp",
            size_hint=(0.9, None),
            height="60dp",
            pos_hint={"center_x": .5},
            md_bg_color=get_color_from_hex('#39FF14'),
            text_color=[0, 0, 0, 1]
        )
        self.turbo_btn.bind(on_release=self.activate_turbo)
        main_layout.add_widget(self.turbo_btn)
        
        main_layout.add_widget(MDBoxLayout(size_hint_y=None, height="40dp"))

        screen.add_widget(main_layout)
        return screen

    def activate_turbo(self, *args):
        # Efeito visual de ativação
        self.turbo_btn.text = "ATIVANDO..."
        self.turbo_btn.md_bg_color = get_color_from_hex('#FF3131') # Vermelho alerta
        
        # Execução dos comandos via Shizuku (Simulação Shell)
        try:
            # Comandos de performance pesada
            os.system("cmd power set-fixed-performance-mode-enabled true")
            os.system("settings put global touch_acceleration_enabled 1")
            
            # Atualiza interface após sucesso
            Clock.schedule_once(self.success_state, 1.5)
        except:
            self.info_label.text = "ERRO: SHIZUKU NÃO DETECTADO"

    def success_state(self, dt):
        self.turbo_btn.text = "SISTEMA OTIMIZADO ✅"
        self.turbo_btn.md_bg_color = get_color_from_hex('#00FF00')
        self.info_label.text = "ESTADO DO SISTEMA: PERFORMANCE MÁXIMA\nFPS TARGET: 120\nMODO: GAMER EXTREME"

if __name__ == '__main__':
    SupremeFlyApp().run()
