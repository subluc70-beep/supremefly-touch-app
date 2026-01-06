import flet as ft

def main(page: ft.Page):
    # Configurações básicas de visualização
    page.title = "SUPREME TOUCH"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#050505"
    # Centralização total
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Elementos da interface
    icone = ft.Icon(ft.icons.TARGET, size=100, color="#39FF14")
    texto = ft.Text("SUPREME TOUCH ATIVO", size=24, color="white", weight="bold")
    
    btn = ft.ElevatedButton(
        "TESTAR SISTEMA",
        width=250,
        height=60,
        style=ft.ButtonStyle(
            bgcolor="#1A1A1A",
            color="#39FF14",
            shape=ft.RoundedRectangleBorder(radius=10)
        )
    )

    # Organizando na tela
    page.add(
        ft.Column(
            [
                icone,
                texto,
                ft.Divider(height=20, color="transparent"),
                btn,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    
    page.update()

# O SEGREDO PARA NÃO FICAR TELA PRETA NO ANDROID:
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.FLET_APP)
