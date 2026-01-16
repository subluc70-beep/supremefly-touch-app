[app]
# (Pode alterar o nome se quiser)
title = SupremeFly PRO
package.name = supremefly
package.domain = com.supreme.touch
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 3.5
orientation = portrait

# --- Requisitos e Bibliotecas ---
# pyjnius é essencial para o Python falar com o Android/Shizuku
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,pyjnius,requests

# --- Permissões Críticas ---
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, moe.shizuku.manager.permission.API_V23, QUERY_ALL_PACKAGES, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# --- Configurações de Sistema (Onde a mágica acontece) ---
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
android.enable_androidx = True
android.accept_sdk_license = True

# --- ESSENCIAL PARA O SHIZUKU RECONHECER O APP ---
# Isso avisa ao Android que o seu app tem permissão para "procurar" o Shizuku
android.manifest.queries = moe.shizuku.privileged.api, moe.shizuku.manager

# --- Configurações de Tela e Gráficos (Evita Tela Preta) ---
android.presplash_color = #1A1A1A
android.wakelock = True
android.meta_data = com.google.android.gms.version=@integer/google_play_services_version

# --- Configurações do Buildozer ---
[buildozer]
log_level = 2
warn_on_root = 1
build_dir = ./.buildozer
bin_dir = ./bin
