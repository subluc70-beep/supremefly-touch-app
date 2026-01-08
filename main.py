from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.slider import MDSlider
from kivymd.uix.button import MDFillRoundFlatButton, MDRoundFlatIconButton
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.uix.behaviors import DragBehavior
from kivy.uix.behaviors import ButtonBehavior

# Classe para criar o FPS que pode ser arrastado
class DraggableFPS(DragBehavior, MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drag_timeout = 10000000
        self.drag_distance = 0
        self.drag_rectangle = [self.x, self.y, self.width, self.height]

    def on_pos(self, *args):
        self.drag_rectangle = [self.x, self.y, self.width, self.height]

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        Window.clearcolor = get_color_from_hex('#0A0A0A')
        
        self.screen = MDScreen()
        
        # Layout Principal (Fundo)
        layout = MDBoxLayout(orientation='vertical', padding=30, spacing=15)

        # Título
        layout.add_widget(MDLabel(
            text="SUPREME FLY PRO",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=get_color_from_hex('#39FF14')
        ))

        # --- EIXO X ---
        layout.add_widget(MDLabel(text="SENSIBILIDADE HORIZONTAL (X)", halign="center", theme_text_color="Hint"))
        self.label_x = MDLabel(text="0.5 mm", halign="center", font_style="H5")
        self.slider_x = MDSlider(min=0.1, max=1.0, value=0.5, step=0.1, color=get_color_from_hex('#39FF14'))
        self.slider_x.bind(value=self.update_x)
        layout.add_widget(self.label_x)
        layout.add_widget(self.slider_x)

        # --- EIXO Y ---
        layout.add_widget(MDLabel(text="SENSIBILIDADE VERTICAL (Y)", halign="center", theme_text_color="Hint"))
        self.label_y = MDLabel(text="0.5 mm", halign="center", font_style="H5")
        self.slider_y = MDSlider(min=0.1, max=1.0, value=0.5, step=0.1, color=get_color_from_hex('#00E5FF'))
        self.slider_y.bind(value=self.update_y)
        layout.add_widget(self.label_y)
        layout.add_widget(self.slider_y)

        # --- BOTÃO DE CALIBRAÇÃO ---
        self.btn_calibrar = MDRoundFlatIconButton(
            icon="target",
            text="CALIBRAR TOUCH",
            pos_hint={"center_x": .5},
            text_color=get_color_from_hex('#FFFFFF'),
            line_color=get_color_from_hex('#39FF14'),
            size_hint_x=0.9
        )
        self.btn_calibrar.bind(on_press=self.iniciar_calibracao)
        layout.add_widget(self.btn_calibrar)

        # --- CONTADOR DE FPS ARRASTÁVEL ---
        self.fps_widget = DraggableFPS(
            text="FPS: 60",
            size_hint=(None, None),
            size=(100, 50),
            pos=(50, 50), # Posição inicial
            md_bg_color=(0, 0, 0, 0.5), # Fundo pretinho transparente
            theme_text_color="Custom",
            text_color=get_color_from_hex('#39FF14'),
            halign="center"
        )
        
        self.screen.add_widget(layout)
        self.screen.add_widget(self.fps_widget) # Adiciona por cima do layout
        
        Clock.schedule_interval(self.update_fps, 1/30)
        
        return self.screen

    def update_fps(self, dt):
        self.fps_widget.text = f"FPS: {int(Clock.get_fps())}"

    def update_x(self, instance, value):
        self.label_x.text = f"{value:.1f} mm"

    def update_y(self, instance, value):
        self.label_y.text = f"{value:.1f} mm"

    def iniciar_calibracao(self, instance):
        instance.text = "CALIBRANDO..."
        Clock.schedule_once(self.finalizar_calibracao, 2)

    def finalizar_calibracao(self, dt):
        self.btn_calibrar.text = "CALIBRADO!"

if __name__ == '__main__':
    SupremeFlyApp().run()
