[app]
title = Viraj Remote Tap
package.name = remotetap
package.domain = org.viraj
source.dir = .
source.include_exts = py,png,jpg,kv,java,xml
version = 0.1

requirements = python3,kivy,requests,pyjnius,oscpy

orientation = portrait

android.permissions = INTERNET, FOREGROUND_SERVICE, WAKE_LOCK, BIND_ACCESSIBILITY_SERVICE

android.add_src = java/RemoteControl.java

services = Remoteservice:service.py

android.manifest.accessibility_service = """
<service android:name="org.viraj.remotetap.RemoteControl"
         android:permission="android.permission.BIND_ACCESSIBILITY_SERVICE"
         android:exported="true">
    <intent-filter>
        <action android:name="android.accessibilityservice.AccessibilityService" />
    </intent-filter>
    <meta-data android:name="android.accessibilityservice" android:resource="@xml/accessibility_service_config" />
</service>
"""

android.api = 31
android.minapi = 21
android.ndk = 25b