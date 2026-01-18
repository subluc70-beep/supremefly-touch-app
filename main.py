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
            return Builder.load_string(f'MDScreen:\n  MDLabel:\n    text: "{e}"\n    halign: "center"')

    def apply_hardware_logic(self):
        if platform == 'android':
            x = self.root.ids.sensi_x.value / 1000
            y = self.root.ids.sensi_y.value / 1000
            
            # MÉTODOS DE INJEÇÃO
            paths = [
                "/data/local/tmp/rish",
                "/sdcard/Android/data/moe.shizuku.privileged.api/files/rish",
                "rish"
            ]
            
            success = False
            for p in paths:
                cmd = f"sh {p} -c 'settings put global touch.pressure.scale {x} && settings put global touch.size.scale {y}'"
                if os.system(cmd) == 0:
                    success = True
                    break
            
            if success:
                self.root.ids.log_label.text = f"> ATIVO: X={x}"
                self.root.ids.log_label.text_color = [0, 1, 0, 1]
            else:
                self.root.ids.log_label.text = "> ERRO: AUTORIZE NO SHIZUKU"
                self.root.ids.log_label.text_color = [1, 0, 0, 1]
        else:
            self.root.ids.log_label.text = "> MODO DESENVOLVEDOR PC"

if __name__ == '__main__':
    SupremeFlyApp().run()
