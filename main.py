import flet as ft
import subprocess

def main(page: ft.Page):
    # Configurações essenciais para Android
    page.title = "SUPREME TOUCH PRO"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#050505"
    page.padding = 30
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Variáveis de UI
    valor_mm = ft.Text("0.5 mm", size=60, weight="bold", color="#39FF14")
    status_msg = ft.Text("SISTEMA PRONTO", color="grey", size=12, weight="bold")

    def executar_comando(comando):
        try:
            # Tenta executar (requer Shizuku/ADB ativo no celular)
            subprocess.run(comando, shell=True, timeout=5)
            return True
        except:
            return False

    def aplicar_sensibilidade(e):
        btn.disabled = True
        btn.text = "PROCESSANDO..."
        page.update()
        
        mm = slider.value
        pixels = max(1, int(mm * 12))
        
        comandos = [
            f"settings put secure view_configuration_touch_slop {pixels}",
            "settings put global touch_low_latency 1",
            "settings put secure long_press_timeout 150"
        ]
        
        sucesso = True
        for cmd in comandos:
            if not executar_comando(cmd):
                sucesso = False
        
        if sucesso:
            btn.text = "OTIMIZAÇÃO ATIVA"
            btn.bgcolor = "#39FF14"
            btn.color = "black"
            status_msg.value = f"SUCESSO: {mm:.1f}mm APLICADO"
            status_msg.color = "#39FF14"
        else:
            btn.text = "ERRO DE PERMISSÃO"
            btn.bgcolor = "red"
            status_msg.value = "ERRO: SEM ACESSO AO ADB/SHIZUKU"
            status_msg.color = "red"
        
        btn.disabled = False
        page.update()

    # Construção da Interface
    container_principal = ft.Column(
        [
            ft.Icon(ft.icons.TARGET, size=70, color="#39FF14"),
            ft.Text("SUPREME TOUCH", size=24, weight="bold"),
            ft.Text("ANTI-LAG ENGINE", size=10, color="#6200EE"),
            ft.Divider(height=20, color="transparent"),
            valor_mm,
            slider := ft.Slider(
                min=0.1, max=1.0, divisions=9, value=0.5,
                active_color="#39FF14",
                on_change=lambda e: (setattr(valor_mm, "value", f"{e.control.value:.1f} mm"), page.update())
            ),
            status_msg,
            ft.Divider(height=20, color="transparent"),
            btn := ft.ElevatedButton(
                "ATIVAR BLINDAGEM",
                width=280, height=60,
                on_click=aplicar_sensibilidade,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(container_principal)

# IMPORTANTE: Para o APK, o Flet precisa rodar assim:
if __name__ == "__main__":
    ft.app(target=main)
