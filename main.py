import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock

class SupremeFlyApp(MDApp):
    def build(self):
        # Carrega a interface primeiro (Leve)
        return Builder.load_file('principal.kv')

    def on_start(self):
        # AGENDA as funções pesadas para DEPOIS que o app abrir.
        # 5 segundos depois, para dar tempo do Android respirar.
        Clock.schedule_once(self.iniciar_sistema_blindado, 5)

    def iniciar_sistema_blindado(self, dt):
        # Só agora o Python tenta falar com o Shizuku
        try:
            # Em vez de um comando pesado, enviamos um simples 'echo'
            os.system("sh /data/local/tmp/rish -c echo 'ready'")
            self.root.ids.log_label.text = "> HARDWARE PRONTO"
        except:
            self.root.ids.log_label.text = "> ERRO DE CARGA"
