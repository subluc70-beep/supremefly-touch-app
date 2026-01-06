from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.slider import MDSlider
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        Window.clearcolor = get_color_from_hex('#000000')
        screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical', padding=40, spacing=25)
        layout.add_widget(MDLabel(text="SUPREME FLY PRO", halign="center", font_style="H4", text_color=get_color_from_hex('#39FF14'), theme_text_color="Custom"))
        self.label_val = MDLabel(text="0.5 mm", halign="center", font_style="H2")
        self.slider = MDSlider(min=0.1, max=1.0, value=0.5, step=0.1, color=get_color_from_hex('#39FF14'))
        self.slider.bind(value=self.update_val)
        layout.add_widget(self.label_val)
        layout.add_widget(self.slider)
        self.btn = MDFillRoundFlatButton(text="SUAVIZAR TOQUE: OFF", pos_hint={"center_x": .5}, md_bg_color=get_color_from_hex('#1A1A1A'))
        layout.add_widget(self.btn)
        screen.add_widget(layout)
        return screen

    def update_val(self, instance, value):
        self.label_val.text = f"{value:.1f} mm"

if __name__ == '__main__':
    SupremeFlyApp().run()
