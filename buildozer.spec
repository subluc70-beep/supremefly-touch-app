[app]
title = SupremeFly PRO
package.name = supremefly
package.domain = com.supreme.touch
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# ESSENCIAL PARA O SHIZUKU E O VISUAL
requirements = python3,kivy==2.3.0,kivymd,pyjnius,certifi

orientation = portrait
fullscreen = 1

# PERMISSÕES QUE FAZEM O APP APARECER NO SHIZUKU
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, moe.shizuku.manager.permission.API_V23, QUERY_ALL_PACKAGES

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
