import flet as ft
import subprocess

def main(page: ft.Page):
    page.title = "SUPREME TOUCH PRO"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#050505"
    page.padding = 30
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    valor_mm = ft.Text("0.5 mm", size=60, weight="bold", color="#39FF14")
    status_msg = ft.Text("AGUARDANDO PERMISSÃO", color="grey", size=12, weight="bold")

    def aplicar_via_shizuku(e):
        btn.disabled = True
        btn.text = "SOLICITANDO ACESSO..."
        page.update()
        
        mm = slider.value
        pixels = max(1, int(mm * 12))
        
        # O SEGREDO: Usamos o 'rish' para invocar o Shizuku
        # Isso faz o sistema abrir o pedido de permissão!
        comando_base = f"settings put secure view_configuration_touch_slop {pixels}"
        comando_shizuku = f"sh /sdcard/android/data/moe.shizuku.privileged.api/files/rish -c '{comando_base}'"
        
        try:
            # Ao rodar isso, o Shizuku deve despertar e perguntar se você permite
            processo = subprocess.run(comando_shizuku, shell=True, capture_output=True, text=True)
            
            if processo.returncode == 0:
                btn.text = "PERMISSÃO ACEITA!"
                btn.bgcolor = "#39FF14"
                btn.color = "black"
                status_msg.value = "SUCESSO: SENSIBILIDADE ALTERADA!"
                status_msg.color = "#39FF14"
            else:
                btn.text = "PERMISSÃO NEGADA"
                btn.bgcolor = "red"
                status_msg.value = "ATIVE O SHIZUKU ANTES DE CLICAR"
        except:
            status_msg.value = "ERRO AO ACESSAR O SHIZUKU"
            
        btn.disabled = False
        page.update()

    # UI básica (mesma estrutura que você já conhece)
    page.add(
        ft.Icon(ft.icons.BOLT, size=70, color="#39FF14"),
        ft.Text("SUPREME TOUCH", size=24, weight="bold"),
        ft.Divider(height=20, color="transparent"),
        valor_mm,
        slider := ft.Slider(min=0.1, max=1.0, divisions=9, value=0.5, active_color="#39FF14",
            on_change=lambda e: (setattr(valor_mm, "value", f"{e.control.value:.1f} mm"), page.update())),
        status_msg,
        ft.Divider(height=20, color="transparent"),
        btn := ft.ElevatedButton("ATIVAR VIA SHIZUKU", width=280, height=60, on_click=aplicar_via_shizuku)
    )

if __name__ == "__main__":
    ft.app(target=main)
