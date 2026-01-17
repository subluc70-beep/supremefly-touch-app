import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import platform

class SupremeFlyApp(MDApp):
    def build(self):
        # Define o tema antes de carregar a interface
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        
        # Carrega o arquivo KV completo
        try:
            self.root_widget = Builder.load_file('principal.kv')
            return self.root_widget
        except Exception as e:
            # Caso o arquivo KV falhe, cria uma tela de erro para o app não fechar
            return Builder.load_string(f'''
MDScreen:
    md_bg_color: 0,0,0,1
    MDLabel:
        text: "ERRO AO CARREGAR INTERFACE:\\n{str(e)}"
        halign: "center"
        theme_text_color: "Error"
''')

    def apply_hardware_logic(self):
        """Função que força o Shizuku a reconhecer o app e injeta a sensi"""
        if platform == 'android':
            try:
                # Pega os valores reais dos sliders
                x = self.root_widget.ids.sensi_x.value / 1000
                y = self.root_widget.ids.sensi_y.value / 1000
                
                # O COMANDO MESTRE: Tenta rodar via 'rish' no local padrão
                # Isso forçará o Shizuku a notar a tentativa de acesso
                comando = f"sh /data/local/tmp/rish -c 'settings put global touch.pressure.scale {x} && settings put global touch.size.scale {y}'"
                
                resultado = os.system(comando)
                
                if resultado == 0:
                    self.root_widget.ids.log_label.text = f"> SUCESSO: X={x} Y={y}"
                    self.root_widget.ids.log_label.text_color = [0, 1, 0, 1]
                else:
                    # Se falhar, é porque o Shizuku não autorizou ainda
                    self.root_widget.ids.log_label.text = "> ERRO: AUTORIZE O APP NO SHIZUKU"
                    self.root_widget.ids.log_label.text_color = [1, 0, 0, 1]
                    
            except Exception as e:
                self.root_widget.ids.log_label.text = f"> ERRO: {str(e)}"
        else:
            self.root_widget.ids.log_label.text = "> ERRO: RODAR NO ANDROID"

if __name__ == '__main__':
    SupremeFlyApp().run()
