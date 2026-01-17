import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import platform

# Força o carregamento do arquivo KV
try:
    Builder.load_string(open('principal.kv', encoding='utf-8').read())
except Exception as e:
    print(f"Erro ao ler arquivo KV: {e}")

class SupremeFlyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return # O Builder já carregou a tela

    def apply_hardware_logic(self):
        """A função só roda quando você clica, evitando fechar sozinho"""
        try:
            # Puxa valores da interface com segurança
            x = self.root.ids.sensi_x.value / 1000
            y = self.root.ids.sensi_y.value / 1000
            
            # Tenta falar com o Shizuku apenas neste momento
            if platform == 'android':
                # Comando 'rish' - Caminho padrão do Shizuku
                os.system(f"sh /data/local/tmp/rish -c 'settings put global touch.pressure.scale {x}'")
                self.root.ids.log_label.text = f"> INJETADO: {x}"
            else:
                self.root.ids.log_label.text = "> ERRO: RODAR NO ANDROID"
                
        except Exception as e:
            self.root.ids.log_label.text = f"> ERRO: {str(e)}"

if __name__ == '__main__':
    SupremeFlyApp().run()
