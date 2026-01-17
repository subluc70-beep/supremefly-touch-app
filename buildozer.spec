[app]
# --- Identidade ---
title = SupremeFly Regedit
package.name = supremeflyregedit
package.domain = org.supremefly
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 4.0.0

# --- Requisitos (NÃO TRADUZIR) ---
requirements = python3, kivy==2.3.0, kivymd==1.2.0, pyjnius

orientation = portrait

# --- Permissões e Shizuku (A CHAVE DO RECONHECIMENTO) ---
android.permissions = INTERNET, WRITE_SECURE_SETTINGS, QUERY_ALL_PACKAGES
android.manifest.queries = moe.shizuku.privileged.api
# Esta linha abaixo é essencial para o Shizuku ver o app como "amigo"
android.add_libs = libs/shizuku-api.aar

# --- Configurações de Compilação ---
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.skip_update = False

# --- Inicialização ---
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
