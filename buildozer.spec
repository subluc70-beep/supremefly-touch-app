[app]
title = SupremeFly PRO
package.name = supremefly
package.domain = com.supreme.touch
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 3.6
orientation = portrait

# Adicionamos 'requests' e 'urllib3' para caso precise de updates
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,pyjnius

# Permissões completas para o Moto G30
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, moe.shizuku.manager.permission.API_V23, QUERY_ALL_PACKAGES, WRITE_EXTERNAL_STORAGE

android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
android.enable_androidx = True

# O segredo do Shizuku está aqui:
android.manifest.queries = moe.shizuku.privileged.api, moe.shizuku.manager

# Cor de fundo da inicialização (Pre-splash) para evitar tela branca/preta feia
android.presplash_color = #000000

[buildozer]
log_level = 2
warn_on_root = 1
