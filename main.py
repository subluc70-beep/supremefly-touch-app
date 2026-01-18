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
            return Builder.load_string(f'MDScreen:\n  MDLabel:\n    text: "Erro KV: {e}"\n    halign: "center"')

    def apply_hardware_logic(self):
        if platform == 'android':
            x = self.root.ids.sensi_x.value / 1000
            y = self.root.ids.sensi_y.value / 1000
            
            # Tenta múltiplos métodos de acesso ao Shizuku/rish
            methods = [
                f"sh /data/local/tmp/rish -c 'settings put global touch.pressure.scale {x} && settings put global touch.size.scale {y}'",
                f"rish -c 'settings put global touch.pressure.scale {x} && settings put global touch.size.scale {y}'",
                f"settings put global touch.pressure.scale {x}"
            ]
            
            success = False
            for cmd in methods:
                if os.system(cmd) == 0:
                    success = True
                    break
            
            if success:
                self.root.ids.log_label.text = f"> SUCESSO: X={x}"
                self.root.ids.log_label.text_color = [0, 1, 0, 1]
            else:
                self.root.ids.log_label.text = "> ERRO: VERIFIQUE O SHIZUKU"
                self.root.ids.log_label.text_color = [1, 0, 0, 1]
        else:
            print(f"Simulando: X={self.root.ids.sensi_x.value}")

if __name__ == '__main__':
    SupremeFlyApp().run()
