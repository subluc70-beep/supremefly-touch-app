import flet as ft
import subprocess

def main(page: ft.Page):
    page.title = "SUPREME TOUCH PRO"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#050505"
    page.window_width = 400
    page.window_height = 800
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # UI Elements
    valor_mm = ft.Text("0.5 mm", size=60, weight="bold", color="#39FF14")
    status_msg = ft.Text("SHIZUKU NECESSÁRIO", color="grey", size=12, weight="bold")
    
    def executar_comando_shizuku(comando):
        # Tenta os dois caminhos possíveis do Shizuku (rish direto ou via path)
        caminhos = [
            f"sh /sdcard/android/data/moe.shizuku.privileged.api/files/rish -c '{comando}'",
            f"rish -c '{comando}'"
        ]
        
        for cmd in caminhos:
            try:
                res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=4)
                if res.returncode == 0:
                    return True
            except:
                continue
        return False

    def aplicar_sensibilidade(e):
        btn.disabled = True
        btn.text = "SOLICITANDO ACESSO..."
        page.update()
        
        mm = slider.value
        pixels = max(1, int(mm * 12))
        
        # Lista de comandos para otimização máxima
        comandos = [
            f"settings put secure view_configuration_touch_slop {pixels}",
            "settings put global touch_low_latency 1",
            "settings put system pointer_speed 7", # Aumenta velocidade do ponteiro
            "settings put secure long_press_timeout 200"
        ]
        
        sucesso = False
        for cmd in comandos:
            if executar_comando_shizuku(cmd):
                sucesso = True
        
        if sucesso:
            btn.text = "SISTEMA OTIMIZADO"
            btn.bgcolor = "#39FF14"
            btn.color = "black"
            status_msg.value = f"TOUCH SLOP DEFINIDO PARA {pixels}px"
            status_msg.color = "#39FF14"
        else:
            btn.text = "ERRO: SHIZUKU OFF"
            btn.bgcolor = "#FF0000"
            status_msg.value = "ATIVE O SHIZUKU E DÊ PERMISSÃO"
            status_msg.color = "red"
            
        btn.disabled = False
        page.update()

    # --- LAYOUT ---
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Icon(ft.icons.TARGET, size=80, color="#39FF14"),
                ft.Text("SUPREME TOUCH PRO", size=26, weight="bold"),
                ft.Text("V4.5 - SHIZUKU ENGINE", size=10, color="grey"),
                ft.Divider(height=40, color="transparent"),
                ft.Text("AJUSTE DE SENSIBILIDADE", size=14),
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
                    width=300, height=70,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                    on_click=aplicar_sensibilidade
                ),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
