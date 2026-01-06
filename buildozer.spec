[app]
title = SupremeFly PRO
package.name = supremefly
package.domain = com.supreme.touch
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.3
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pyjnius,certifi
orientation = portrait
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, moe.shizuku.manager.permission.API_V23, QUERY_ALL_PACKAGES
android.api = 33
android.archs = arm64-v8a, armeabi-v7a
[buildozer]
log_level = 2
