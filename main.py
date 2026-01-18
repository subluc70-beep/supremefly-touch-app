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
            return Builder.load_string(f'MDScreen:\n  MDLabel:\n    text: "Erro: {e}"\n    halign: "center"')

    def apply_optimization(self):
        if platform == 'android':
            x = self.root.ids.sensi_x.value / 1000
            y = self.root.ids.sensi_y.value / 1000
            
            # MÉTODOS DE INJEÇÃO REDUNDANTES
            cmds = [
                f"sh /data/local/tmp/rish -c 'settings put global touch.pressure.scale {x}'",
                f"sh /data/local/tmp/rish -c 'settings put global touch.size.scale {y}'",
                f"rish -c 'settings put global touch.pressure.scale {x}'",
                f"settings put global touch.pressure.scale {x}" 
            ]
            
            success = False
            for cmd in cmds:
                if os.system(cmd) == 0:
                    success = True
            
            if success:
                self.root.ids.log_status.text = f"> SUCESSO: {x}"
                self.root.ids.log_status.text_color = [0, 1, 0, 1]
            else:
                self.root.ids.log_status.text = "> ERRO: USE O SHIZUKU"
                self.root.ids.log_status.text_color = [1, 0, 0, 1]
        else:
            self.root.ids.log_status.text = "> TESTE PC OK"

if __name__ == '__main__':
    SupremeFlyApp().run()
