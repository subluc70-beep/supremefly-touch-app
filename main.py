import flet as ft

def main(page: ft.Page):
    page.title = "SUPREME FLY"
    page.bgcolor = "#050505"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Icon(ft.icons.TARGET, size=100, color="#39FF14"),
        ft.Text("SUPREME FLY ATIVO", size=24, color="white", weight="bold"),
        ft.ElevatedButton(
            "CONECTAR SISTEMA",
            width=250,
            style=ft.ButtonStyle(bgcolor="#1A1A1A", color="#39FF14")
        )
    )
    page.update()
if __name__ == "__main__":
    # Mudamos para o modo que mais funciona em celulares com bloqueio de rede
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
