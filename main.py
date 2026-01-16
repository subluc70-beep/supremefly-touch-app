from kivy.lang import Builder

# Isso força o Python a ler o arquivo de design que você criou
Builder.load_file('principal.kv')

class SupremeFlyApp(MDApp):
    def build(self):
        return # O Builder já carregou a tela
from kivymd.app import MDApp
import os

class SupremeFlyApp(MDApp):
    def build(self):
        # O Kivy carrega o main.kv automaticamente
        pass

    def apply_logic(self):
        # Puxa os dados da interface sem esforço
        x = self.root.ids.sensi_x.value
        y = self.root.ids.sensi_y.value
        prio = self.root.ids.switch_prio.active
        
        # A matemática pura aqui
        val_x = x / 1000
        val_y = y / 1000
        
        # Injeção via Shizuku
        os.system(f"shizuku_session settings put global touch.pressure.scale {val_x}")
        print(f"Calculado e Aplicado: X={val_x}")

if __name__ == '__main__':
    SupremeFlyApp().run()
