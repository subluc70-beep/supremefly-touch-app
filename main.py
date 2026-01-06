import flet as ft

def main(page: ft.Page):
    # Configurações para garantir que a UI apareça
    page.bgcolor = "#050505"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Criando os componentes antes de adicionar
    icone = ft.Icon(ft.icons.TARGET, size=80, color="#39FF14")
    titulo = ft.Text("SUPREME TOUCH PRO", size=26, weight="bold", color="white")
    
    # Botão de teste simples
    btn_teste = ft.ElevatedButton(
        "ATIVAR SISTEMA", 
        width=250, 
        height=60,
        style=ft.ButtonStyle(bgcolor="#1A1A1A", color="#39FF14")
    )

    # Adicionando tudo dentro de uma coluna centralizada
    page.add(
        ft.Column(
            [
                icone,
                titulo,
                ft.Divider(height=20, color="transparent"),
                btn_teste,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    
    # Força a atualização da página
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
