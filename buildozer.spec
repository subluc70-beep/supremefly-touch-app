[app]
# (Atenção: Use sem tradutor ligado)
title = SupremeFly Regedit
package.name = supremeflyregedit
package.domain = org.supremefly
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 4.0.0

# REQUISITOS (Versões travadas para evitar crash)
requirements = python3, kivy==2.3.0, kivymd==1.2.0, pyjnius

orientation = portrait

# PERMISSÕES PARA O MOTO G30
android.permissions = INTERNET, WRITE_SECURE_SETTINGS, QUERY_ALL_PACKAGES

# CONFIGURAÇÃO DE RECONHECIMENTO DO SHIZUKU
android.manifest.queries = moe.shizuku.privileged.api

android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.skip_update = False
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
