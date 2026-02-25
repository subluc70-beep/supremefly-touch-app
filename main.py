import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import platform

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file('principal.kv')

    def apply_optimization(self):
        if platform == 'android':
            # Conversão precisa para escala do Android
            val_x = self.root.ids.sensi_x.value / 1000
            val_y = self.root.ids.sensi_y.value / 1000
            
            # Comandos de Hardware (Sensibilidade de Pressão e Tamanho do Toque)
            cmd = (f"settings put global touch.pressure.scale {val_x} && "
                   f"settings put global touch.size.scale {val_y}")
            
            # Lista de execução prioritária (API Shizuku -> ADB -> Shell)
            methods = [
                f"sh /data/local/tmp/rish -c '{cmd}'", # Método Nativo Shizuku
                f"rish -c '{cmd}'",                   # Atalho Shizuku
                f"su -c '{cmd}'",                     # Fallback Root
                cmd                                   # Fallback ADB direto
            ]
            
            success = False
            for m in methods:
                if os.system(m) == 0:
                    success = True
                    break
            
            if success:
                self.root.ids.log_status.text = f"> HARDWARE OTIMIZADO: {val_x}"
                self.root.ids.log_status.text_color = [0, 1, 0, 1]
            else:
                self.root.ids.log_status.text = "> ERRO: REINICIE O SHIZUKU"
                self.root.ids.log_status.text_color = [1, 0, 0, 1]
        else:
            print("Executando em ambiente de testes (PC)")

if __name__ == '__main__':
    SupremeFlyApp().run()
