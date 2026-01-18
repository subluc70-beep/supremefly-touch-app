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

    def check_shizuku_permission(self):
        if platform == 'android':
            try:
                # Acessa a API do Shizuku via Java
                Shizuku = autoclass('moe.shizuku.privileged.api.Shizuku')
                PackageManager = autoclass('android.content.pm.PackageManager')
                
                if Shizuku.pingBinder():
                    # Verifica se já temos permissão
                    if Shizuku.checkSelfPermission() == PackageManager.PERMISSION_GRANTED:
                        return True
                    else:
                        # Solicita permissão nativa (abrirá o popup do Shizuku)
                        Shizuku.requestPermission(0)
                        return False
                else:
                    return False
            except Exception:
                return False
        return True

    def apply_optimization(self):
        if platform == 'android':
            if self.check_shizuku_permission():
                x = self.root.ids.sensi_x.value / 1000
                y = self.root.ids.sensi_y.value / 1000
                
                # Usando o Shizuku para executar o shell nativo de forma persistente
                cmd_x = f"settings put global touch.pressure.scale {x}"
                cmd_y = f"settings put global touch.size.scale {y}"
                
                # Execução via Binder Nativo
                os.system(f"sh /data/local/tmp/rish -c '{cmd_x} && {cmd_y}'")
                
                self.root.ids.log_status.text = "> CONECTADO VIA API NATIVA"
                self.root.ids.log_status.text_color = [0, 1, 0, 1]
            else:
                self.root.ids.log_status.text = "> AGUARDANDO PERMISSÃO..."
                self.root.ids.log_status.text_color = [1, 1, 0, 1]

if __name__ == '__main__':
    SupremeFlyApp().run()
