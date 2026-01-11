[app]
title = SupremeFly PRO
package.name = supremefly
package.domain = com.supreme.touch
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.8
orientation = portrait

# BIBLIOTECAS ESSENCIAIS
requirements = python3,hostpython3,kivy==2.3.0,kivymd==1.2.0,pillow,pyjnius,cython==0.29.33,sdl2_image,sdl2_ttf

# PERMISSÕES E SHIZUKU (Ajustado para reconhecer o app)
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, moe.shizuku.manager.permission.API_V23, QUERY_ALL_PACKAGES
android.manifest.queries = moe.shizuku.privilege.api
android.gradle_dependencies = "dev.rikka.shizuku:api:13.1.0", "dev.rikka.shizuku:provider:13.1.0"

# CONFIGURAÇÕES DE SISTEMA
android.api = 33
android.minapi = 21
android.ndk = 25c
android.archs = arm64-v8a, armeabi-v7a
android.skip_update = False
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
