[app]
title = SupremeFly Touch
package.name = supremeflytouch
package.domain = org.supremefly
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 6.0.0

requirements = python3, kivy==2.3.0, kivymd==1.2.0, pyjnius, pillow

orientation = portrait

# Permissões totais para injeção de hardware
android.permissions = INTERNET, WRITE_SECURE_SETTINGS, QUERY_ALL_PACKAGES, FOREGROUND_SERVICE

# Queries para o Shizuku não ser bloqueado pelo Android 11+
android.manifest.queries = moe.shizuku.privileged.api

android.api = 33
android.minapi = 29
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
