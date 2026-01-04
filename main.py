import flet as ft

def main(page: ft.Page):
    page.title = "Supreme Fly Touch"
    page.add(ft.Text("App Funcionando!"))

if __name__ == "__main__":
    ft.app(target=main)
