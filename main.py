from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.slider import MDSlider
from kivymd.uix.button import MDFillRoundFlatButton, MDRoundFlatIconButton
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        Window.clearcolor = get_color_from_hex('#0A0A0A')
        
        screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical', padding=30, spacing=15)

        # Título Neon
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
            text="CALIBRAR TOUCH (REDUZIR LAG)",
            pos_hint={"center_x": .5},
            text_color=get_color_from_hex('#FFFFFF'),
            line_color=get_color_from_hex('#39FF14'),
            size_hint_x=0.9
        )
        self.btn_calibrar.bind(on_press=self.iniciar_calibracao)
        layout.add_widget(self.btn_calibrar)

        # Botão Suavizar
        self.btn_suavizar = MDFillRoundFlatButton(
            text="SUAVIZAR TOQUE: OFF",
            pos_hint={"center_x": .5},
            md_bg_color=get_color_from_hex('#1A1A1A'),
            size_hint_x=0.9
        )
        self.btn_suavizar.bind(on_press=self.toggle_suavizar)
        layout.add_widget(self.btn_suavizar)

        screen.add_widget(layout)
        return screen

    def update_x(self, instance, value):
        self.label_x.text = f"{value:.1f} mm"

    def update_y(self, instance, value):
        self.label_y.text = f"{value:.1f} mm"

    def iniciar_calibracao(self, instance):
        instance.text = "CALIBRANDO... AGUARDE"
        instance.line_color = get_color_from_hex('#FFD700')
        Clock.schedule_once(self.finalizar_calibracao, 2)

    def finalizar_calibracao(self, dt):
        self.btn_calibrar.text = "TOUCH CALIBRADO!"
        self.btn_calibrar.line_color = get_color_from_hex('#39FF14')

    def toggle_suavizar(self, instance):
        if "OFF" in instance.text:
            instance.text = "SUAVIZAR TOQUE: ON"
            instance.md_bg_color = get_color_from_hex('#39FF14')
        else:
            instance.text = "SUAVIZAR TOQUE: OFF"
            instance.md_bg_color = get_color_from_hex('#1A1A1A')

if __name__ == '__main__':
    SupremeFlyApp().run()
