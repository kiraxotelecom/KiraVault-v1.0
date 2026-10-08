# =============================================================================
# KiraVault — buildozer.spec
# Pure Python + Kivy app, single-arch (arm64-v8a) debug APK.
# Tuned for GitHub Actions on ubuntu-latest.
# =============================================================================

[app]

# ------------------------------------------------------------------ identity
title = KiraVault
package.name = kiravault
package.domain = com.kiravault
version = 1.0.0

# ------------------------------------------------------------------ source
# Source code location (repo root — the folder containing main.py)
source.dir = .

# Only include the file types your app actually uses.
# NOTE: Do NOT set source.include_patterns — it overrides include_exts
#       and would silently drop your .py files.
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf

# Never ship these.
source.exclude_exts = spec,log,md,txt,bak,pyc

# Keep the APK small — skip build caches and dev folders.
source.exclude_dirs = tests,bin,venv,.venv,.buildozer,__pycache__,backups,.git,.github

# Extra safety.
source.exclude_patterns = license,LICENSE,*.bak,*.log,*.pyc

# ------------------------------------------------------------------ assets
# App icon (MUST exist in the repo root as my_icon.png, 512x512 recommended).
icon.filename = %(source.dir)s/my_icon.png

# Uncomment when you have a presplash image:
# presplash.filename = %(source.dir)s/assets/presplash.png

# ------------------------------------------------------------------ ui
orientation = portrait
fullscreen = 0

# ------------------------------------------------------------------ deps
requirements = python3,kivy==2.3.0,pyjnius,plyer,android

# ------------------------------------------------------------------ android
# API 33 = Android 13. minapi 24 = Android 7.0 (covers ~98% of devices).
android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24
android.archs = arm64-v8a

# Auto-accept the SDK license so the CI build never hangs on a prompt.
android.accept_sdk_license = True

# Permissions used by reminders + autobackup.
android.permissions = POST_NOTIFICATIONS, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Android Auto Backup (separate from autobackup.py — a second safety net).
android.allow_backup = True

# Debug builds produce an APK; release builds would produce an AAB.
android.debug_artifact = apk
# android.release_artifact = aab

# ------------------------------------------------------------------ p4a
# Use the upstream python-for-android master branch (default).
# p4a.branch = master

# ------------------------------------------------------------------ logging
[buildozer]
log_level = 2
warn_on_root = 1