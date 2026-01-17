import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.utils import platform

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        # Carrega o design externo
        return Builder.load_file('principal.kv')

    def apply_hardware_logic(self):
        """Executa a matemática e injeta via Shizuku"""
        try:
            # Captura valores dos sliders
            x_val = self.root.ids.sensi_x.value / 1000
            y_val = self.root.ids.sensi_y.value / 1000
            
            # Feedback visual imediato
            self.root.ids.log_label.text = f"> INJETANDO X:{x_val} Y:{y_val}"
            
            if platform == 'android':
                # Comando mestre via rish (Shizuku)
                # settings put global é o nível mais profundo de hardware
                cmd_x = f"sh /data/local/tmp/rish -c 'settings put global touch.pressure.scale {x_val}'"
                cmd_y = f"sh /data/local/tmp/rish -c 'settings put global touch.size.scale {y_val}'"
                
                os.system(cmd_x)
                os.system(cmd_y)
                
                self.root.ids.log_label.text = "> HARDWARE ATUALIZADO!"
                self.root.ids.log_label.text_color = [0.2, 1, 0, 1]
        except Exception as e:
            self.root.ids.log_label.text = f"> ERRO: {str(e)}"

if __name__ == '__main__':
    SupremeFlyApp().run()
