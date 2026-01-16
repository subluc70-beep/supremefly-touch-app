import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock

# Isso liga o seu arquivo de design ao código
Builder.load_file('principal.kv')

class SupremeFlyApp(MDApp):
    def build(self):
        # Aqui o Python carrega a interface do principal.kv
        return 

    def on_start(self):
        """Isso roda assim que o app abre para o Shizuku reconhecer"""
        Clock.schedule_once(self.check_shizuku, 1)

    def check_shizuku(self, dt):
        try:
            # Comando simples para forçar o pop-up de permissão do Shizuku
            os.system("shizuku_session echo 'Conectado'")
            self.root.ids.log_label.text = "> SHIZUKU SINCRONIZADO"
        except:
            self.root.ids.log_label.text = "> ERRO: ATIVE O SHIZUKU"

    def apply_hardware_logic(self):
        """A função matemática que você pediu"""
        # Puxando os valores diretamente dos IDs que criamos no principal.kv
        x_raw = self.root.ids.sensi_x.value
        y_raw = self.root.ids.sensi_y.value
        prio_active = self.root.ids.switch_prio.active

        # Conversão para escala nativa (0.0 a 1.0)
        x_final = x_raw / 1000
        y_final = y_raw / 1000
        prio_val = 1.0 if prio_active else 0.0

        try:
            # Injeção via Shizuku (Comando Shell Nativo)
            os.system(f"shizuku_session settings put global touch.pressure.scale {x_final}")
            os.system(f"shizuku_session settings put global touch.size.scale {y_final}")
            os.system(f"shizuku_session settings put global touch.filter.abscenter {prio_val}")
            
            self.root.ids.log_label.text = f"> APLICADO: X:{x_final} Y:{y_final}"
            self.root.ids.log_label.theme_text_color = "Custom"
            self.root.ids.log_label.text_color = [0, 1, 0, 1] # Verde se der certo
        except:
            self.root.ids.log_label.text = "> ERRO NA INJEÇÃO"

if __name__ == '__main__':
    SupremeFlyApp().run()
