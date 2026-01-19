import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import platform
from jnius import autoclass, cast

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file('principal.kv')

    def check_shizuku_api(self):
        if platform == 'android':
            try:
                # Classes Nativa do Shizuku via JNI
                Shizuku = autoclass('moe.shizuku.privileged.api.Shizuku')
                PackageManager = autoclass('android.content.pm.PackageManager')
                
                if Shizuku.pingBinder():
                    if Shizuku.checkSelfPermission() == PackageManager.PERMISSION_GRANTED:
                        return "OK"
                    else:
                        Shizuku.requestPermission(0)
                        return "SOLICITANDO"
                else:
                    return "DESLIGADO"
            except Exception as e:
                return f"ERRO_API: {str(e)}"
        return "PC_MODE"

    def apply_optimization(self):
        status = self.check_shizuku_api()
        if status == "OK":
            x = self.root.ids.sensi_x.value / 1000
            y = self.root.ids.sensi_y.value / 1000
            
            # Comando enviado através do túnel do Shizuku
            cmd = f"settings put global touch.pressure.scale {x} && settings put global touch.size.scale {y}"
            os.system(f"sh /data/local/tmp/rish -c '{cmd}'")
            
            self.root.ids.log_status.text = f"> CONECTADO: ESCALA {x}"
            self.root.ids.log_status.text_color = [0, 1, 0, 1]
        elif status == "SOLICITANDO":
            self.root.ids.log_status.text = "> ACEITE A PERMISSÃO NO POPUP"
            self.root.ids.log_status.text_color = [1, 1, 0, 1]
        else:
            self.root.ids.log_status.text = f"> STATUS: {status}"
            self.root.ids.log_status.text_color = [1, 0, 0, 1]

if __name__ == '__main__':
    SupremeFlyApp().run()
