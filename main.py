[app]
title = Insta Manager
package.name = instamanager
package.domain = com.sirfjimmy.instamanager
source.dir = .
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True
p4a.branch = master
android.permissions = INTERNET
