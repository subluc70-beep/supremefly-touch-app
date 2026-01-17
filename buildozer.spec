[app]
title = SupremeFly Regedit
package.name = supremeflyregedit
package.domain = org.supremefly
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 3.5.0

# REQUISITOS (Lembre-se: NÃO traduzir para requisitos)
requirements = python3, kivy==2.3.0, kivymd==1.2.0, pillow, pyjnius

orientation = portrait

# PERMISSÕES (NÃO traduzir para permissões)
android.permissions = INTERNET, WRITE_SECURE_SETTINGS, QUERY_ALL_PACKAGES, FOREGROUND_SERVICE

# PERMITIR QUE O APP VEJA O SHIZUKU
android.manifest.queries = moe.shizuku.privileged.api

android.api = 31
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
