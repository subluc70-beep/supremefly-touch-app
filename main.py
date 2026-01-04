import flet as ft

def main(page: ft.Page):
    page.title = "Supreme Fly Touch"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Supreme Fly Touch", size=30, weight="bold"),
                    ft.Text("O App foi construído com sucesso!", size=18),
                    ft.Icon(ft.icons.CHECK_CIRCLE, color="green", size=50),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
