from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import os

class SupremeFlyApp(App):
    def build(self):
        # Fundo Preto Puro
        Window.clearcolor = get_color_from_hex('#000000')
        layout = BoxLayout(orientation='vertical', padding=40, spacing=25)

        # Cabeçalho
        layout.add_widget(Label(
            text='SUPREME FLY PRO',
            font_size='34sp',
            bold=True,
            color=get_color_from_hex('#39FF14') # Verde Neon
        ))

        # Indicador de Valor Atual
        layout.add_widget(Label(text='SENSIBILIDADE ATUAL', font_size='14sp', color=(1,1,1,0.5)))
        
        # Barra de 0.1 a 1.0
        self.slider = Slider(min=0.1, max=1.0, value=0.5, step=0.1)
        self.val_label = Label(text=f'{self.slider.value:.1f} mm', font_size='45sp', bold=True, color=get_color_from_hex('#00E5FF'))
        self.slider.bind(value=self.atualizar_contagem)
        
        layout.add_widget(self.slider)
        layout.add_widget(self.val_label)

        # Botão Suavizar Toque (O Toque Reto)
        self.btn_suavizar = Button(
            text='SUAVIZAR TOQUE: OFF',
            size_hint=(1, 0.2),
            background_normal='',
            background_color=get_color_from_hex('#151515'),
            color=(1, 1, 1, 1)
        )
        self.btn_suavizar.bind(on_press=self.toggle_suavizar)
        layout.add_widget(self.btn_suavizar)

        # Botão Shizuku (Chamada de Sistema)
        self.btn_shizuku = Button(
            text='VINCULAR AO SHIZUKU',
            size_hint=(1, 0.2),
            background_normal='',
            background_color=get_color_from_hex('#39FF14'),
            color=(0, 0, 0, 1),
            bold=True
        )
        self.btn_shizuku.bind(on_press=self.chamar_shizuku)
        layout.add_widget(self.btn_shizuku)

        return layout

    def atualizar_contagem(self, instance, value):
        self.val_label.text = f'{value:.1f} mm'

    def toggle_suavizar(self, instance):
        if instance.text == 'SUAVIZAR TOQUE: OFF':
            instance.text = 'SUAVIZAR TOQUE: ON'
            instance.background_color = get_color_from_hex('#00E5FF')
            instance.color = (0, 0, 0, 1)
        else:
            instance.text = 'SUAVIZAR TOQUE: OFF'
            instance.background_color = get_color_from_hex('#151515')
            instance.color = (1, 1, 1, 1)

    def chamar_shizuku(self, instance):
        instance.text = "SOLICITANDO..."
        # Comando para forçar o serviço do Shizuku a reconhecer o App
        os.system("pm list packages --user 0") 
        os.system("sh /sdcard/Android/data/moe.shizuku.manager/files/start.sh")

if __name__ == '__main__':
    SupremeFlyApp().run()
