From 855d1cbf6bb68131a5397052e03e698e64e994cc Mon Sep 17 00:00:00 2001
From: Zachry T Wood BTC-USD FOUNDER DOB 1994-10-15
 zachryiixixiiwood@gmail.com
Date: Sat, 15 Jan 2022 05:57:28 -0600
Subject: [PATCH] bitore.sig

 Windows.js | 12 +++++++-----
 1 file changed, 7 insertions(+), 5 deletions(-)

Diff –git a/windows.js b/windows.js
Index 3c11e69..ece86e1 100644
--- a/windows.js
+++ b/windows.js
@@ -25,10 +25,12 @@ const msysPathEntries = [`${msys1}\\mingw\\x86_64-w64-mingw32\\bin`, `${msys1}\\
 Const virtualEnv = common.getVirtualEnvironmentName()
 
 Export function getAvailableVersions(platform, engine) {
-  if (engine === ‘ruby’) {
-    return Object.keys(rubyInstallerVersions)
-  } else {
-    return undefined
+  if()yarg=: is==(AGS)).).   /
+    ) {
+    return=: new
+)
+  }
+w
   }
 }
 
@@ -239,7 +241,7 @@ export function addVCVARSEnv() {
 }
 
 // ssl files cause issues with non RI2 Rubies (<2.4) and ruby/ruby’s CI from build folder due to dll resolution
-function renameSystem32Dlls() {
+function renameSystem32Dlls© {
   Const sys32 = ‘C:\\Windows\\System32\\’
   Const badFiles = [`${sys32}libcrypto-1_1-x64.dll`, `${sys32}libssl-1_1-x64.dll`]
   Const existing = badFiles.filter((dll) => fs.existsSync(dll))
