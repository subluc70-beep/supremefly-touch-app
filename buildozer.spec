[app]
title = SupremeFly
package.name = supremefly
package.domain = com.supreme
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,certifi
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, moe.shizuku.manager.permission.API_V23
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
