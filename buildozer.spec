[app]
title = SupremeFly PRO
package.name = supremefly
package.domain = com.supreme.touch
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 2.1
orientation = portrait

# REQUIREMENTS (Removi versões fixas para deixar o Buildozer escolher as melhores de 2026)
requirements = python3,kivy,kivymd,pillow,pyjnius

# SHIZUKU & PERMISSÕES
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, moe.shizuku.manager.permission.API_V23, QUERY_ALL_PACKAGES
android.manifest.queries = moe.shizuku.privilege.api
android.gradle_dependencies = dev.rikka.shizuku:api:13.1.0, dev.rikka.shizuku:provider:13.1.0

# APIS E NDK (Ajustado para o servidor do GitHub 2026)
android.api = 34
android.minapi = 21
android.ndk = 27b
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
