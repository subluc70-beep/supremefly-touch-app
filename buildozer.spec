[app]
# --- Identidade do App ---
title = SupremeFly Regedit
package.name = supremeflyregedit
package.domain = org.supremefly
version = 3.2.0

# --- Arquivos Incluídos ---
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
# IMPORTANTE: Garante que o principal.kv seja empacotado
source.include_patterns = assets/*,*.kv

# --- Requisitos (VERSÕES TRAVADAS PARA NÃO CRASHAR) ---
requirements = python3, kivy==2.3.0, kivymd==1.2.0, pillow, pyjnius

orientation = portrait

# --- Permissões de Sistema (Blindagem) ---
# WRITE_SECURE_SETTINGS: Permite a injeção de sensibilidade
# QUERY_ALL_PACKAGES: Permite enxergar o Shizuku
android.permissions = INTERNET, WRITE_SECURE_SETTINGS, QUERY_ALL_PACKAGES, FOREGROUND_SERVICE, PACKAGE_USAGE_STATS

# --- Configuração Shizuku (O segredo do reconhecimento) ---
android.manifest.queries = moe.shizuku.privileged.api

# --- Configuração de Hardware (Moto G30) ---
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# --- Ajustes de Inicialização ---
# Força o Android a não fechar o app por "demora no carregamento"
android.skip_update = False
android.accept_sdk_license = True
android.entrypoint = main.py

# --- Ícones (Opcional) ---
# icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
