[app]
title = SupremeFly PRO
package.name = supremefly
package.domain = com.supreme.touch
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.5

# MUDANÇA AQUI: Cython fixo nos requirements
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pyjnius,certifi,cython==0.29.33

orientation = portrait
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, moe.shizuku.manager.permission.API_V23, QUERY_ALL_PACKAGES
android.api = 33
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
