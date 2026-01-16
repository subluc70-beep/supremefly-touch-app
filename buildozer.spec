[app]
title = SupremeFly Regedit
# Nome sem underline para evitar erros de registro no Shizuku
package.name = supremeflyregedit
package.domain = org.supremefly
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 3.1.0

# Requisitos blindados
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,pyjnius

orientation = portrait

# Permissões completas para controle de hardware e Shizuku
android.permissions = INTERNET, FOREGROUND_SERVICE, PACKAGE_USAGE_STATS, WRITE_SECURE_SETTINGS, QUERY_ALL_PACKAGES

# A "Chave Mestra" para o Shizuku enxergar seu app
android.manifest.queries = moe.shizuku.privileged.api

# Configuração para o hardware do Moto G30 (Android 11-13)
android.api = 33
android.minapi = 21
android.ndk = 25b

# Se você não criou o arquivo monitor_service.py ainda, 
# recomendo comentar a linha abaixo com um # no início para não dar erro no build
# android.services = monitor:monitor_service.py

android.skip_update = False
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
