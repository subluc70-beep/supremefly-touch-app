[app]
title = SupremeFly PRO
package.name = supremefly
package.domain = com.supreme.touch
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.8

# Bibliotecas necessárias para a interface e o sistema
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pyjnius,cython==0.29.33,sdl2_image,sdl2_ttf

orientation = portrait

# --- PERMISSÕES E SHIZUKU ---
# Removi a duplicidade e organizei as permissões
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, moe.shizuku.manager.permission.API_V23, QUERY_ALL_PACKAGES

# Esta linha permite que o Shizuku 'enxergue' seu app
android.manifest.queries = moe.shizuku.privilege.api

# --- CONFIGURAÇÕES DE SISTEMA ---
android.api = 33
android.minapi = 21
android.ndk = 25c
android.ndk_path = 
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.skip_update = False

[buildozer]
log_level = 2
warn_on_root = 1
