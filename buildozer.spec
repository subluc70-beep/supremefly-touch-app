[app]
title = SupremeFly Regedit
package.name = supremeflyregedit
package.domain = org.supremefly
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 5.0.0

requirements = python3, kivy==2.3.0, kivymd==1.2.0, pyjnius

orientation = portrait

# Permissões específicas para Android 11+
android.permissions = INTERNET, WRITE_SECURE_SETTINGS, QUERY_ALL_PACKAGES, FOREGROUND_SERVICE
android.manifest.queries = moe.shizuku.privileged.api

# Foco em dispositivos modernos (64 bits)
android.api = 33
android.minapi = 30
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
