[app]
# (str) Title of your application
title = SupremeFly PRO

# (str) Package name
package.name = supremefly

# (str) Package domain (needed for android packaging)
package.domain = com.supreme.touch

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.8

# (list) Application requirements
# Adicionado sdl2_image e sdl2_ttf para garantir a renderização dos botões
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pyjnius,cython==0.29.33,sdl2_image,sdl2_ttf

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) Permissions
# Estas são as permissões que permitem o app encontrar e usar o Shizuku
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, moe.shizuku.manager.permission.API_V23, QUERY_ALL_PACKAGES

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25c

# (str) Android NDK directory (if empty, it will be automatically downloaded)
android.ndk_path = 

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) indicates whether the screen should stay on
# Useful for games to prevent the screen from sleeping
android.skip_update = False

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess downloads or save time
android.accept_sdk_license = True

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
