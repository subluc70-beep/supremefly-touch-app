from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class SupremeFlyApp(App):
    def build(self):
        # Configuração da Janela
        Window.clearcolor = get_color_from_hex('#0a0a0a')
        
        layout = BoxLayout(orientation='vertical', padding=50, spacing=30)
        
        # Título Estilizado
        self.label = Label(
            text='SUPREME FLY',
            font_size='40sp',
            bold=True,
            color=get_color_from_hex('#39FF14') # Verde Neon
        )
        
        # Subtítulo informativo
        self.status = Label(
            text='Status: Pronto para Otimizar',
            font_size='16sp',
            color=(1, 1, 1, 0.7)
        )
        
        # Botão Principal
        btn = Button(
            text='ATIVAR OTIMIZAÇÃO',
            size_hint=(1, 0.3),
            background_normal='',
            background_color=get_color_from_hex('#1a1a1a'),
            color=(1, 1, 1, 1),
            bold=True
        )
        btn.bind(on_press=self.ativar)

        layout.add_widget(self.label)
        layout.add_widget(self.status)
        layout.add_widget(btn)
        
        return layout

    def ativar(self, instance):
        self.label.text = "SISTEMA ATIVO"
        self.status.text = "Sensibilidade Otimizada com Sucesso!"
        self.label.color = get_color_from_hex('#14ccff') # Muda para Azul ao ativar

if __name__ == '__main__':
    SupremeFlyApp().run()
