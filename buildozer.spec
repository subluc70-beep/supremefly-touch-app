[app]
# (str) Title of your application
title = SupremeFly PRO

# (str) Package name
package.name = supremefly

# (str) Package domain
package.domain = com.supreme.touch

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.8

# (list) Application requirements
# Incluído pillow e hostpython3 para evitar crashes na interface
requirements = python3,hostpython3,kivy==2.3.0,kivymd==1.2.0,pillow,pyjnius,cython==0.29.33,sdl2_image,sdl2_ttf

# (str) Supported orientation
orientation = portrait

# --- CONFIGURAÇÕES ANDROID E SHIZUKU ---
# Permissões necessárias para o Shizuku e Alerta de Sistema
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, moe.shizuku.manager.permission.API_V23, QUERY_ALL_PACKAGES

# Linha vital para o Shizuku reconhecer o app no Android 11+
android.manifest.queries = moe.shizuku.privilege.api

# Versões de API e NDK recomendadas para estabilidade no GitHub Actions
android.api = 33
android.minapi = 21
android.ndk = 25c
android.ndk_path = 

# Arquiteturas para rodar na maioria dos celulares (64 e 32 bits)
android.archs = arm64-v8a, armeabi-v7a

# Pular atualizações desnecessárias do SDK para acelerar o build
android.skip_update = False
android.accept_sdk_license = True

[buildozer]
# Nível de log 2 para vermos todos os detalhes se der erro
log_level = 2
warn_on_root = 1
