import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import platform
from kivy.clock import Clock

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        # Carrega a interface externa
        try:
            return Builder.load_file('principal.kv')
        except Exception as e:
            return Builder.load_string(f'MDScreen:\n  MDLabel:\n    text: "Erro ao carregar KV: {e}"\n    halign: "center"')

    def apply_optimization(self):
        if platform == 'android':
            # Valores convertidos para escala de hardware
            val_x = self.root.ids.sensi_x.value / 1000
            val_y = self.root.ids.sensi_y.value / 1000
            
            # LISTA DE TODOS OS MÉTODOS PARA RECONHECER O SHIZUKU
            # 1. Via rish no diretório temporário (Padrão Shizuku)
            # 2. Via rish direto no PATH (Se o usuário configurou rish)
            # 3. Via comando direto 'settings' (Alguns modelos Android 10 aceitam)
            
            cmds = [
                f"sh /data/local/tmp/rish -c 'settings put global touch.pressure.scale {val_x}'",
                f"sh /data/local/tmp/rish -c 'settings put global touch.size.scale {val_y}'",
                f"rish -c 'settings put global touch.pressure.scale {val_x}'",
                f"settings put global touch.pressure.scale {val_x}"
            ]
            
            success = False
            for cmd in cmds:
                result = os.system(cmd)
                if result == 0:
                    success = True
            
            if success:
                self.root.ids.log_status.text = f"> SUPREMEFLY ATIVADO: {val_x}"
                self.root.ids.log_status.text_color = [0, 1, 0, 1] # Verde
            else:
                self.root.ids.log_status.text = "> ERRO: REATIVE O SHIZUKU"
                self.root.ids.log_status.text_color = [1, 0, 0, 1] # Vermelho
        else:
            self.root.ids.log_status.text = "> EXECUTANDO EM MODO PC"

if __name__ == '__main__':
    SupremeFlyApp().run()
