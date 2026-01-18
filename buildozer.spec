[app]
title = SupremeFly Touch
package.name = supremeflytouch
package.domain = org.supremefly
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 7.5.0

requirements = python3, kivy==2.3.0, kivymd==1.2.0, pyjnius, pillow

orientation = portrait

# Permissões Críticas
android.permissions = INTERNET, WRITE_SECURE_SETTINGS, QUERY_ALL_PACKAGES, FOREGROUND_SERVICE
# Necessário para Android 11+ ver o Shizuku
android.manifest.queries = moe.shizuku.privileged.api

# Ajustes de Compilação
android.api = 33
android.minapi = 29
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.enable_androidx = True
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
