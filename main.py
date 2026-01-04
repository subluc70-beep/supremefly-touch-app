import flet as ft

def main(page: ft.Page):
    # Configurações de página para garantir que apareça algo
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Criando um cartão visual para não ter erro de tela vazia
    cartao_principal = ft.Container(
        content=ft.Column([
            ft.Icon(ft.icons.SETTINGS_SUGGEST, color=ft.colors.BLUE, size=50),
            ft.Text("SUPREME SENSI", size=30, weight="bold", color=ft.colors.WHITE),
            ft.Text("Otimizador de Sensibilidade", color=ft.colors.GREY_400),
            ft.Divider(height=20),
            ft.ElevatedButton("ATIVAR SENSI IOS", bgcolor=ft.colors.BLUE, color=ft.colors.WHITE, width=250),
            ft.ElevatedButton("LIMPAR LAG", bgcolor=ft.colors.GREY_800, color=ft.colors.WHITE, width=250),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=40,
        bgcolor=ft.colors.GREY_900,
        border_radius=20,
        border=ft.border.all(1, ft.colors.BLUE_700)
    )

    page.add(cartao_principal)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
