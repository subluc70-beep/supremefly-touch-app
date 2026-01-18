[app]
title = SupremeFly Touch
package.name = supremeflytouch
package.domain = org.supremefly
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 6.1.0

# Pillow e Pyjnius são essenciais para interface e Shizuku
requirements = python3, kivy==2.3.0, kivymd==1.2.0, pyjnius, pillow

orientation = portrait

# Permissões e Queries (Shizuku)
android.permissions = INTERNET, WRITE_SECURE_SETTINGS, QUERY_ALL_PACKAGES, FOREGROUND_SERVICE
android.manifest.queries = moe.shizuku.privileged.api

# CONFIGURAÇÕES DE COMPILAÇÃO (O segredo do erro está aqui)
android.api = 33
android.minapi = 29
android.ndk = 25b
android.ndk_path = 
android.sdk_path = 
# Compilando apenas para 64 bits para evitar conflitos de biblioteca no build
android.archs = arm64-v8a
android.accept_sdk_license = True
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
