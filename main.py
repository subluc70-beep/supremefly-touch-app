import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import platform

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        try:
            return Builder.load_file('principal.kv')
        except Exception as e:
            return Builder.load_string(f'<MDScreen><MDLabel text="Erro no Design: {e}" halign="center" theme_text_color="Error"/></MDScreen>')

    def apply_hardware_logic(self):
        if platform == 'android':
            try:
                # Valores dos Sliders
                x = self.root.ids.sensi_x.value / 1000
                y = self.root.ids.sensi_y.value / 1000
                
                # No Android 11+, o rish costuma estar neste local ou no PATH
                # Tentamos o comando via rish (Shizuku)
                comando = f"sh /data/local/tmp/rish -c 'settings put global touch.pressure.scale {x} && settings put global touch.size.scale {y}'"
                
                resultado = os.system(comando)
                
                if resultado == 0:
                    self.root.ids.log_label.text = f"> SUCESSO: SENSI APLICADA (X:{x})"
                    self.root.ids.log_label.text_color = [0, 1, 0, 1]
                else:
                    self.root.ids.log_label.text = "> ERRO: AUTORIZE NO APP SHIZUKU"
                    self.root.ids.log_label.text_color = [1, 0, 0, 1]
            except Exception as e:
                self.root.ids.log_label.text = f"> FALHA NO HARDWARE: {str(e)}"
        else:
            self.root.ids.log_label.text = "> STATUS: MODO DESENVOLVEDOR PC"

if __name__ == '__main__':
    SupremeFlyApp().run()
