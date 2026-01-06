display_name: Supreme Touch
product_name: supreme_touch
executable_name: supreme_touch
bundle_id: com.seu.supremetouch
version: 1.0.0
build_number: 1

android:
  permissions:
    - INTERNET
    - QUERY_ALL_PACKAGES
    - SYSTEM_ALERT_WINDOW
  # Isso evita que o Android tente "otimizar" o app e cause a tela preta
  intent_filters:
    - action: android.intent.action.MAIN
      category: android.intent.category.LAUNCHER
