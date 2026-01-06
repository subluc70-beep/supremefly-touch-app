from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class SupremeFlyApp(App):
    def build(self):
        # Definindo a cor de fundo (Preto escuro)
        Window.clearcolor = (0.02, 0.02, 0.02, 1)
        
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        # Título
        self.label = Label(
            text='SUPREME FLY',
            font_size='32sp',
            bold=True,
            color=(0.22, 1, 0.08, 1) # Verde Neon
        )
        
        # Botão de Ativação
        btn = Button(
            text='CONECTAR SISTEMA',
            size_hint=(1, 0.2),
            background_color=(0.1, 0.1, 0.1, 1),
            color=(1, 1, 1, 1)
        )
        btn.bind(on_press=self.ativar)

        layout.add_widget(self.label)
        layout.add_widget(btn)
        
        return layout

    def ativar(self, instance):
        self.label.text = "SISTEMA ATIVO!"
        self.label.color = (1, 1, 1, 1)

if __name__ == '__main__':
    SupremeFlyApp().run()
