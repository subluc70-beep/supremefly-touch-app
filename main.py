import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import platform

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file('principal.kv')

    def check_shizuku_status(self):
        if platform == 'android':
            from jnius import autoclass
            try:
                Shizuku = autoclass('moe.shizuku.privileged.api.Shizuku')
                if Shizuku.pingBinder():
                    PackageManager = autoclass('android.content.pm.PackageManager')
                    if Shizuku.checkSelfPermission() == PackageManager.PERMISSION_GRANTED:
                        return "CONECTADO"
                    else:
                        Shizuku.requestPermission(0)
                        return "AGUARDANDO PERMISSÃO"
                return "SHIZUKU DESLIGADO"
            except Exception as e:
                return f"ERRO API: {str(e)}"
        return "MODO DESENVOLVEDOR"

    def apply_optimization(self):
        status = self.check_shizuku_status()
        self.root.ids.log_status.text = f"> {status}"
        
        if status == "CONECTADO":
            x = self.root.ids.sensi_x.value / 1000
            y = self.root.ids.sensi_y.value / 1000
            # Comando via shell autorizado pelo binder
            os.system(f"sh /data/local/tmp/rish -c 'settings put global touch.pressure.scale {x} && settings put global touch.size.scale {y}'")
            self.root.ids.log_status.text = f"> OTIMIZADO: {x}"
            self.root.ids.log_status.text_color = [0, 1, 0, 1]

if __name__ == '__main__':
    SupremeFlyApp().run()
