from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.slider import MDSlider
from kivymd.uix.button import MDRaisedButton, MDFillRoundFlatButton
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from jnius import autoclass

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        Window.clearcolor = get_color_from_hex('#050505')
        
        screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical', padding=30, spacing=20)

        # Título Neon
        layout.add_widget(MDLabel(
            text="SUPREME FLY PRO",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=get_color_from_hex('#39FF14')
        ))

        # Slider Milimétrico (0.1 - 1.0)
        layout.add_widget(MDLabel(text="SENSIBILIDADE (mm)", halign="center"))
        self.slider = MDSlider(min=0.1, max=1.0, value=0.5, step=0.1, color=get_color_from_hex('#39FF14'))
        self.label_val = MDLabel(text=f"{self.slider.value:.1f} mm", halign="center", font_style="H5")
        self.slider.bind(value=self.update_val)
        
        layout.add_widget(self.slider)
        layout.add_widget(self.label_val)

        # Botão Suavizar Toque (Toque Reto)
        self.btn_suavizar = MDFillRoundFlatButton(
            text="SUAVIZAR TOQUE: OFF",
            pos_hint={"center_x": .5},
            md_bg_color=get_color_from_hex('#1A1A1A')
        )
        self.btn_suavizar.bind(on_press=self.toggle_suavizar)
        layout.add_widget(self.btn_suavizar)

        screen.add_widget(layout)
        return screen

    def on_start(self):
        # Tenta conectar ao Shizuku AUTOMATICAMENTE ao abrir o app
        self.check_shizuku_permission()

    def update_val(self, instance, value):
        self.label_val.text = f"{value:.1f} mm"

    def toggle_suavizar(self, instance):
        if "OFF" in instance.text:
            instance.text = "SUAVIZAR TOQUE: ON"
            instance.md_bg_color = get_color_from_hex('#00E5FF')
        else:
            instance.text = "SUAVIZAR TOQUE: OFF"
            instance.md_bg_color = get_color_from_hex('#1A1A1A')

    def check_shizuku_permission(self):
        # Código para disparar a permissão oficial do Shizuku
        try:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            currentActivity = PythonActivity.mActivity
            PackageManager = autoclass('android.content.pm.PackageManager')
            
            # Tenta verificar se o Shizuku permite o acesso
            # Isso dispara a janela oficial "Allow SupremeFly to access Shizuku?"
            permission = "moe.shizuku.manager.permission.API_V23"
            check = currentActivity.checkSelfPermission(permission)
            
            if check != PackageManager.PERMISSION_GRANTED:
                currentActivity.requestPermissions([permission], 1)
        except Exception as e:
            print(f"Shizuku Error: {e}")

if __name__ == '__main__':
    SupremeFlyApp().run()
