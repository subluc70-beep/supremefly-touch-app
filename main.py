from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class SupremeFlyApp(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#0a0a0a')
        
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Título
        layout.add_widget(Label(
            text='SUPREME FLY PRO',
            font_size='32sp',
            bold=True,
            color=get_color_from_hex('#39FF14')
        ))

        # --- Área de Regulagem ---
        layout.add_widget(Label(text='Regulagem de Sensibilidade (mm)', font_size='14sp'))
        
        self.mm_slider = Slider(min=0, max=100, value=50, step=1)
        self.mm_label = Label(text=f'{int(self.mm_slider.value)} mm', color=get_color_from_hex('#14ccff'))
        
        self.mm_slider.bind(value=self.atualizar_label)
        
        layout.add_widget(self.mm_slider)
        layout.add_widget(self.mm_label)

        # --- Botão Shizuku ---
        self.btn_shizuku = Button(
            text='PEDIR PERMISSÃO SHIZUKU',
            size_hint=(1, 0.2),
            background_normal='',
            background_color=get_color_from_hex('#222222'),
            color=(1, 1, 1, 1)
        )
        self.btn_shizuku.bind(on_press=self.solicitar_shizuku)
        layout.add_widget(self.btn_shizuku)

        # Botão Ativar
        self.btn_ativar = Button(
            text='ATIVAR OTIMIZAÇÃO',
            size_hint=(1, 0.2),
            background_normal='',
            background_color=get_color_from_hex('#39FF14'),
            color=(0, 0, 0, 1),
            bold=True
        )
        layout.add_widget(self.btn_ativar)
        
        return layout

    def atualizar_label(self, instance, value):
        self.mm_label.text = f'{int(value)} mm'

    def solicitar_shizuku(self, instance):
        # Aqui o app tenta "cutucar" o Shizuku
        # No Android, isso dispara a janela de permissão
        self.btn_shizuku.text = "AGUARDANDO SHIZUKU..."
        self.btn_shizuku.background_color = get_color_from_hex('#ffaa00')
        print("Solicitando acesso ao Shizuku via Binder...")

if __name__ == '__main__':
    SupremeFlyApp().run()
