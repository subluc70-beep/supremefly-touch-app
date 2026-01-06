[app]
# Nome do App na tela do celular
title = SupremeFly PRO
# Nome interno (sem espaços)
package.name = supremefly
# Domínio da sua marca
package.domain = com.supreme.touch
# Onde está o seu main.py
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# REQUISITOS (O coração do app)
# Adicionamos o KivyMD para o visual bonito e Pyjnius para o Shizuku
requirements = python3,kivy==2.3.0,kivymd,pyjnius,certifi

orientation = portrait
fullscreen = 1

# PERMISSÕES (O que permite o app agir no sistema)
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, moe.shizuku.manager.permission.API_V23, QUERY_ALL_PACKAGES

# CONFIGURAÇÕES DE ANDROID
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.skip_update = False
android.accept_sdk_license = True

# Arquiteturas (Para rodar em qualquer celular Android)
android.archs = arm64-v8a, armeabi-v7a

# Ícones e Preservação (Opcional, mas deixa profissional)
# android.preserve_path = False

[buildozer]
log_level = 2
warn_on_root = 1

[pythonforandroid]
# Força o uso do design material
p4a.branch = master
