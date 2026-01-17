import os
import sys
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import platform
from kivy.clock import Clock

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        # Carregamento seguro da interface
        try:
            self.screen = Builder.load_file('principal.kv')
            return self.screen
        except Exception as e:
            return Builder.load_string(f'MDScreen:\n  MDLabel:\n    text: "Erro Crítico: {e}"\n    halign: "center"\n    theme_text_color: "Error"')

    def apply_hardware_logic(self):
        if platform == 'android':
            x = self.root.ids.sensi_x.value / 1000
            y = self.root.ids.sensi_y.value / 1000
            
            # LISTA DE TODOS OS MÉTODOS POSSÍVEIS DE COMANDO
            # Tentamos rish em diferentes diretórios e comandos de sistema
            commands = [
                f"sh /data/local/tmp/rish -c 'settings put global touch.pressure.scale {x}'",
                f"/data/local/tmp/rish -c 'settings put global touch.size.scale {y}'",
                f"sh /sdcard/Android/data/moe.shizuku.privileged.api/files/rish -c 'settings put global touch.pressure.scale {x}'",
                f"rish -c 'settings put global touch.pressure.scale {x}'",
                f"settings put global touch.pressure.scale {x}" # Tentativa direta
            ]
            
            success_count = 0
            for cmd in commands:
                try:
                    result = os.system(cmd)
                    if result == 0:
                        success_count += 1
                except:
                    continue
            
            if success_count > 0:
                self.root.ids.log_label.text = f"> CONEXÃO ATIVA: {x}"
                self.root.ids.log_label.text_color = [0, 1, 0, 1]
            else:
                self.root.ids.log_label.text = "> ERRO: AUTORIZE O APP NO SHIZUKU"
                self.root.ids.log_label.text_color = [1, 0, 0, 1]
        else:
            self.root.ids.log_label.text = "> AMBIENTE DE TESTE (PC)"

if __name__ == '__main__':
    SupremeFlyApp().run()
