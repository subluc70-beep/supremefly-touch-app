from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class SupremeFlyApp(App):
    def build(self):
        # Cor de fundo escura para poupar RAM e bateria
        Window.clearcolor = get_color_from_hex('#050505')
        
        layout = BoxLayout(orientation='vertical', padding=40, spacing=25)
        
        # Título Neon
        layout.add_widget(Label(
            text='SUPREME FLY PRO',
            font_size='35sp',
            bold=True,
            color=get_color_from_hex('#39FF14')
        ))

        # --- Ajuste de Sensibilidade ---
        layout.add_widget(Label(text='Regulação de Sensibilidade', font_size='18sp'))
        
        # Slider de 0 a 100mm
        self.slider = Slider(min=0, max=100, value=50, step=1)
        self.val_label = Label(text=f'{int(self.slider.value)} mm', font_size='25sp', color=get_color_from_hex('#14ccff'))
        
        self.slider.bind(value=self.atualizar_texto)
        
        layout.add_widget(self.slider)
        layout.add_widget(self.val_label)

        # --- Botão Shizuku ---
        self.btn_shizuku = Button(
            text='VINCULAR AO SHIZUKU',
            size_hint=(1, 0.3),
            background_normal='',
            background_color=get_color_from_hex('#1a1a1a'),
            color=(1, 1, 1, 1)
        )
        self.btn_shizuku.bind(on_press=self.conectar_shizuku)
        layout.add_widget(self.btn_shizuku)

        return layout

    def atualizar_texto(self, instance, value):
        self.val_label.text = f'{int(value)} mm'

    def conectar_shizuku(self, instance):
        # Este comando tenta comunicar com o serviço Shizuku
        self.btn_shizuku.text = "A SOLICITAR ACESSO..."
        self.btn_shizuku.background_color = get_color_from_hex('#ffaa00')
        # Log interno para o sistema detectar a tentativa de ligação
        print("Tentando conexão com moe.shizuku.manager.permission.API_V23")

if __name__ == '__main__':
    SupremeFlyApp().run()
