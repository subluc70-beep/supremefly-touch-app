[app]
title = SupremeFly PRO
package.name = supremefly
package.domain = com.supreme.touch
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 3.0
orientation = portrait

requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,pyjnius

android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, moe.shizuku.manager.permission.API_V23, QUERY_ALL_PACKAGES
android.api = 33
android.minapi = 21
android.ndk = 25c
android.archs = arm64-v8a
android.enable_androidx = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
