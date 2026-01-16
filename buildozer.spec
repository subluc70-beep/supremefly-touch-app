[app]
# (Seção básica)
title = SupremeFly Regedit
package.name = supremefly_regedit
package.domain = org.supremefly
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 3.0.0

# --- REQUISITOS (Fundamental para o KivyMD e Shizuku) ---
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,pyjnius

# --- ORIENTAÇÃO ---
orientation = portrait

# --- PERMISSÕES (A "Blindagem") ---
# INTERNET: Necessário para o ADB Wireless
# FOREGROUND_SERVICE: Para o Auto-Reset não morrer em segundo plano
# PACKAGE_USAGE_STATS: Para detectar quando o jogo foi fechado
# WRITE_SECURE_SETTINGS: Para injetar DPI e Pointer Speed
android.permissions = INTERNET, FOREGROUND_SERVICE, PACKAGE_USAGE_STATS, WRITE_SECURE_SETTINGS, QUERY_ALL_PACKAGES

# --- AJUSTES DO MANIFESTO (Específico para Shizuku no Android 11+) ---
# Isso permite que seu app "veja" o app do Shizuku instalado
android.manifest.queries = moe.shizuku.privileged.api

# --- API LEVELS ---
# Android 11 é API 30. O Moto G30 suporta até API 33/34
android.api = 33
android.minapi = 21
android.ndk = 25b

# --- SERVIÇO DE MONITORAMENTO ---
# Isso permite que o app continue vigiando se o jogo fechou
android.services = monitor:monitor_service.py

# --- OTIMIZAÇÃO DE TELA ---
android.skip_update = False
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

# --- ICONES E SPLASH (Opcional - preencha se tiver os arquivos) ---
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/splash.png

[buildozer]
log_level = 2
warn_on_root = 1
