import os
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

# Otimização para evitar tela preta
os.environ['KIVY_GL_BACKEND'] = 'sdl2'

class RedZoneVisual(Widget):
    """Desenha o círculo central da Red Zone"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0, 1, 0, 0.1)  # Verde muito suave (fundo do círculo)
            self.bg_circle = Ellipse(pos=(0, 0), size=(200, 200))
            Color(0, 1, 0, 1)    # Verde Neon (borda)
            self.line_circle = Line(circle=(0, 0, 100), width=2)
        
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        center_x = self.center_x
        center_y = self.center_y
        self.bg_circle.pos = (center_x - 100, center_y - 100)
        self.line_circle.circle = (center_x, center_y, 100)

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        
        screen = MDScreen()
        
        # Layout Principal com scroll simulado ou espaçamento ajustado
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=5)

        # Cabeçalho
        layout.add_widget(MDLabel(
            text="SUPREMEFLY REGEDIT [V3]",
            halign="center", font_style="H5", 
            text_color=get_color_from_hex('#39FF14'),
            theme_text_color="Custom", size_hint_y=None, height="50dp"
        ))

        # Interface do Círculo (Red Zone)
        layout.add_widget(RedZoneVisual(size_hint_y=0.4))

        # --- Área de Ajustes (4 Sliders até 1000) ---
        
        # Eixo X Principal
        layout.add_widget(self.build_slider_label("SENSI EIXO X (GERAL)"))
        self.val_x = MDLabel(text="500", halign="right", theme_text_color="Primary")
        layout.add_widget(self.val_x)
        self.slider_x = MDSlider(min=0, max=1000, value=500, color=get_color_from_hex('#39FF14'))
        self.slider_x.bind(value=lambda i, v: setattr(self.val_x, 'text', str(int(v))))
        layout.add_widget(self.slider_x)

        # Eixo Y Principal
        layout.add_widget(self.build_slider_label("SENSI EIXO Y (VERTICAL)"))
        self.val_y = MDLabel(text="500", halign="right", theme_text_color="Primary")
        layout.add_widget(self.val_y)
        self.slider_y = MDSlider(min=0, max=1000, value=500, color=get_color_from_hex('#39FF14'))
        self.slider_y.bind(value=lambda i, v: setattr(self.val_y, 'text', str(int(v))))
        layout.add_widget(self.slider_y)

        # Eixo X Fino (Ajuste de Red Zone)
        layout.add_widget(self.build_slider_label("RED ZONE X (PRECISÃO)"))
        self.val_rz_x = MDLabel(text="500", halign="right", theme_text_color="Primary")
        layout.add_widget(self.val_rz_x)
        self.slider_rz_x = MDSlider(min=0, max=1000, value=500, color=get_color_from_hex('#39FF14'))
        self.slider_rz_x.bind(value=lambda i, v: setattr(self.val_rz_x, 'text', str(int(v))))
        layout.add_widget(self.slider_rz_x)

        # Eixo Y Fino (Ajuste de Red Zone)
        layout.add_widget(self.build_slider_label("RED ZONE Y (ESTABILIDADE)"))
        self.val_rz_y = MDLabel(text="500", halign="right", theme_text_color="Primary")
        layout.add_widget(self.val_rz_y)
        self.slider_rz_y = MDSlider(min=0, max=1000, value=500, color=get_color_from_hex('#39FF14'))
        self.slider_rz_y.bind(value=lambda i, v: setattr(self.val_rz_y, 'text', str(int(v))))
        layout.add_widget(self.slider_rz_y)

        # Botão de Aplicar via Shizuku
        from kivymd.uix.button import MDFillRoundFlatButton
        btn_apply = MDFillRoundFlatButton(
            text="SALVAR REGEDIT NO SISTEMA",
            pos_hint={"center_x": .5},
            md_bg_color=get_color_from_hex('#39FF14'),
            text_color=[0, 0, 0, 1],
            size_hint_x=0.8
        )
        btn_apply.bind(on_release=self.apply_to_system)
        layout.add_widget(btn_apply)

        screen.add_widget(layout)
        return screen

    def build_slider_label(self, text):
        return MDLabel(text=text, theme_text_color="Secondary", font_style="Caption", size_hint_y=None, height="20dp")

    def apply_to_system(self, *args):
        # Captura os valores de 0 a 1000
        x, y = int(self.slider_x.value), int(self.slider_y.value)
        rz_x, rz_y = int(self.slider_rz_x.value), int(self.slider_rz_y.value)
        
        try:
            # Comandos via Shizuku/Shell para modificar a resposta do touch
            # Nota: pointer_speed no Android vai de -7 a 7, então mapeamos o valor de 1000
            mapped_speed = int((x / 1000) * 14) - 7
            os.system(f"settings put global pointer_speed {mapped_speed}")
            os.system("cmd power set-fixed-performance-mode-enabled true")
            
            print(f"Aplicado: X:{x} Y:{y} RZ_X:{rz_x} RZ_Y:{rz_y}")
        except:
            pass

if __name__ == '__main__':
    SupremeFlyApp().run()
