import flet as ft

def main(page: ft.Page):
    page.title = "Supreme Fly Touch - Store"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 700
    page.vertical_alignment = ft.MainAxisAlignment.START
    
    # Função para os botões
    def abrir_link(e):
        # Aqui você pode colocar o link do seu Discord ou Loja
        page.launch_url("https://discord.gg/SEU_CONVITE")

    # Cabeçalho
    header = ft.Container(
        content=ft.Column([
            ft.Icon(ft.icons.SHOPPING_BAG_ROUNDED, size=50, color=ft.colors.BLUE_ACCENT),
            ft.Text("SUPREME FLY TOUCH", size=24, weight="bold"),
            ft.Text("A melhor loja do Discord", size=14, color=ft.colors.GREY_400),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=30,
    )

    # Botões de Ação
    botoes = ft.Column([
        ft.ElevatedButton(
            "Ver Catálogo de Produtos", 
            icon=ft.icons.LIST_ALT, 
            width=300,
            on_click=abrir_link
        ),
        ft.ElevatedButton(
            "Suporte Via Discord", 
            icon=ft.icons.DISCORD, 
            width=300,
            on_click=abrir_link
        ),
        ft.ElevatedButton(
            "Minha Conta / Aluguel", 
            icon=ft.icons.PERSON, 
            width=300,
            on_click=abrir_link
        ),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15)

    # Rodapé
    footer = ft.Text("Versão 1.0.0 - Oficial", size=10, color=ft.colors.GREY_700)

    page.add(
        ft.Column([
            header,
            ft.Divider(height=20, color=ft.colors.TRANSPARENT),
            botoes,
            ft.Divider(height=40, color=ft.colors.TRANSPARENT),
            footer
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    ft.app(target=main)
