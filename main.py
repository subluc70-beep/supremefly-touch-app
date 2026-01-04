import flet as ft
import subprocess
import os

def main(page: ft.Page):
    # --- CONFIGURAÇÕES DA INTERFACE ---
    page.title = "SUPREME TOUCH PRO"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#050505"
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # --- ELEMENTOS VISUAIS ---
    valor_mm = ft.Text("0.5 mm", size=60, weight="bold", color="#39FF14")
    status_msg = ft.Text("SISTEMA PRONTO", color="grey", size=12, weight="bold")
    
    # --- MOTOR DE EXECUÇÃO (COMANDO ADB) ---
    def executar_comando_adb(comando):
        try:
            # Envia o comando para o shell do sistema
            resultado = subprocess.run(
                comando, 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=5
            )
            return resultado.returncode == 0
        except Exception:
            return False

    def aplicar_sensibilidade(e):
        btn.disabled = True
        btn.text = "PROCESSANDO..."
        page.update()
        
        # Converte o valor do slider para pixels (Ajuste de sensibilidade)
        mm_selecionado = slider.value if slider.value else 0.5
        pixels = max(1, int(mm_selecionado * 12))
        
        # Lista de comandos que alteram a alma do touch no Android
        comandos = [
            f"settings put secure view_configuration_touch_slop {pixels}",
            "settings put global touch_low_latency 1",
            "settings put system pointer_speed 0",
            "settings put secure long_press_timeout 150"
        ]
        
        sucesso_total = True
        for cmd in comandos:
            if not executar_comando_adb(cmd):
                sucesso_total = False
                break
        
        # Resposta visual para o usuário
        if sucesso_total:
            btn.text = "OTIMIZAÇÃO ATIVA"
            btn.bgcolor = "#39FF14"
            btn.color = "black"
            status_msg.value = f"SUCESSO: {mm_selecionado:.1f}mm APLICADO"
            status_msg.color = "#39FF14"
        else:
            btn.text = "FALHA DE PERMISSÃO"
            btn.bgcolor = "#FF0000"
            status_msg.value = "ERRO: ATIVE O SHIZUKU ANTES"
            status_msg.color = "red"
        
        btn.disabled = False
        page.update()

    # --- MONTAGEM DA TELA ---
    header = ft.Column([
        ft.Icon(ft.icons.SHIELD_CHECKED_ROUNDED, size=50, color="#39FF14"),
        ft.Text("SUPREME TOUCH PRO", size=22, weight="bold"),
        ft.Text("ENGINE V4.0 - ANTI-CRASH", size=10, color="#6200EE"),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    slider = ft.Slider(
        min=0.1, max=1.0, divisions=9, value=0.5,
        active_color="#39FF14",
        on_change=lambda e: (setattr(valor_mm, "value", f"{e.control.value:.1f} mm"), page.update())
    )

    btn = ft.ElevatedButton(
        "ATIVAR BLINDAGEM",
        width=280, height=60,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
        on_click=aplicar_sensibilidade
    )

    page.add(
        header,
        ft.Divider(height=40, color="transparent"),
        ft.Text("AJUSTE DE SENSIBILIDADE:", size=12),
        valor_mm,
        slider,
        status_msg,
        ft.Divider(height=20, color="transparent"),
        btn
    )

if __name__ == "__main__":
    ft.app(target=main)
