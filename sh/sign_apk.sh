#!/bin/sh

# 0, cp here
cp -i ./android/unaligned.apk .

# 1, sign
jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 -keystore mini_keystore -storepass '111' -keypass '222'  unaligned.apk key_name -tsa http://timestamp.digicert.com

# 2, verify
jarsigner -sigalg SHA256withRSA -digestalg SHA-256 -keystore mini_keystore -storepass '111' -keypass '222'  unaligned.apk key_name -tsa http://timestamp.digicert.com -verify

# 3, zipalign
echo "to create finalApp.apk ..."
$ANDROID_HOME/build-tools/20.0.0/zipalign 4 unaligned.apk finalApp.apk

# end
echo "end."

