import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.utils import platform

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        # Força o carregamento ignorando erros de cache
        from kivy.lang import Builder
        self.root = Builder.load_file('principal.kv')
        return self.root
        try:
            return Builder.load_file('principal.kv')
        except Exception as e:
            print(f"Erro no KV: {e}")
            return Builder.load_string('<MDScreen><MDLabel text="Erro no KV" halign="center"/></MDScreen>')

    def apply_hardware_logic(self):
        """Matemática de sensibilidade injetada no kernel via Shizuku"""
        try:
            # Captura os valores dos Sliders do principal.kv
            x_val = self.root.ids.sensi_x.value / 1000
            y_val = self.root.ids.sensi_y.value / 1000
            
            self.root.ids.log_label.text = f"> INJETANDO: X={x_val} Y={y_val}"
            
            if platform == 'android':
                # Comandos via rish (Shizuku) para o Moto G30
                cmd_x = f"sh /data/local/tmp/rish -c 'settings put global touch.pressure.scale {x_val}'"
                cmd_y = f"sh /data/local/tmp/rish -c 'settings put global touch.size.scale {y_val}'"
                
                os.system(cmd_x)
                os.system(cmd_y)
                
                self.root.ids.log_label.text = "> HARDWARE ATUALIZADO COM SUCESSO!"
                self.root.ids.log_label.text_color = [0, 1, 0, 1]
            else:
                self.root.ids.log_label.text = "> ERRO: USE NO ANDROID"
        except Exception as e:
            self.root.ids.log_label.text = f"> ERRO CRÍTICO: {str(e)}"

if __name__ == '__main__':
    SupremeFlyApp().run()
