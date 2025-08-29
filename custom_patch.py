root@10.0.0.102's password: 
root@vuultimo4k:~# init 4 && sleep 5 && init 3
root@vuultimo4k:~# cp -r /tmp/e2iPlayer-master/IPTVPlayer /usr/lib/enigma2/pytho
n/Plugins/Extensions/
cp: cannot stat '/tmp/e2iPlayer-master/IPTVPlayer': No such file or directory
root@vuultimo4k:~# 
root@vuultimo4k:~# chmod -R 755 /usr/lib/enigma2/python/Plugins/Extensions/IPTVP
layer
chmod: cannot access '/usr/lib/enigma2/python/Plugins/Extensions/IPTVPlayer': No such file or directory
root@vuultimo4k:~# cp -r /tmp/e2iPlayer-master/IPTVPlayer /usr/lib/enigma2/pytho
n/Plugins/Extensions/
cp: cannot stat '/tmp/e2iPlayer-master/IPTVPlayer': No such file or directory
root@vuultimo4k:~# opkg list | grep -i e2iplayer
enigma2-plugin-extensions-e2iplayer-deps - 1.0-r0.2 - Meta package for installing all dependencies for SSS' E2i Player
enigma2-plugin-extensions-e2iplayer-deps-dbg - 1.0-r0.2 - Meta package for installing all dependencies for SSS' E2i Player - Debugging files
enigma2-plugin-extensions-e2iplayer-deps-dev - 1.0-r0.2 - Meta package for installing all dependencies for SSS' E2i Player - Development files
root@vuultimo4k:~# opkg list | grep -i iptv
enigma2-plugin-extensions-bouquetmakerxtream - 192+cfa9342-r0.0 - IPTV bouquet maker
enigma2-plugin-extensions-bouquetmakerxtream-dbg - 192+cfa9342-r0.0 - IPTV bouquet maker - Debugging files
enigma2-plugin-extensions-bouquetmakerxtream-dev - 192+cfa9342-r0.0 - IPTV bouquet maker - Development files
enigma2-plugin-extensions-iptv-org-playlists - 1.0+git10+4d0456a-r0.12 - enigma2-plugin-extensions-iptv-org-playlists version 1.0+gitAUTOINC+4d0456a218-r0
enigma2-plugin-extensions-iptv-org-playlists-dbg - 1.0+git10+4d0456a-r0.12 - enigma2-plugin-extensions-iptv-org-playlists version 1.0+gitAUTOINC+4d0456a218-r0 - Debugging files
enigma2-plugin-extensions-iptv-org-playlists-dev - 1.0+git10+4d0456a-r0.12 - enigma2-plugin-extensions-iptv-org-playlists version 1.0+gitAUTOINC+4d0456a218-r0 - Development files
enigma2-plugin-extensions-iptv-org-playlists-src - 1.0+git10+4d0456a-r0.12 - enigma2-plugin-extensions-iptv-org-playlists version 1.0+gitAUTOINC+4d0456a218-r0 - Source files
enigma2-plugin-extensions-pravoslavietv - 0.2 - IPTV - Soyuz, Spas, Voskresenie, Radonezh
enigma2-plugin-extensions-xklass - 106+dfcab63-r0.11 - IPTV Xtream Codes/XUI One playlists player by KiddaC
enigma2-plugin-extensions-xklass-dbg - 106+dfcab63-r0.11 - IPTV Xtream Codes/XUI One playlists player by KiddaC - Debugging files
enigma2-plugin-extensions-xklass-dev - 106+dfcab63-r0.11 - IPTV Xtream Codes/XUI One playlists player by KiddaC - Development files
enigma2-plugin-extensions-xklass-src - 106+dfcab63-r0.11 - IPTV Xtream Codes/XUI One playlists player by KiddaC - Source files
enigma2-plugin-extensions-xstreamity - 573+7f5be2e-r0.5 - IPTV Xtream Codes playlists player by KiddaC
enigma2-plugin-extensions-xstreamity-dbg - 573+7f5be2e-r0.5 - IPTV Xtream Codes playlists player by KiddaC - Debugging files
enigma2-plugin-extensions-xstreamity-dev - 573+7f5be2e-r0.5 - IPTV Xtream Codes playlists player by KiddaC - Development files
enigma2-plugin-extensions-xstreamity-src - 573+7f5be2e-r0.5 - IPTV Xtream Codes playlists player by KiddaC - Source files
enigma2-plugin-systemplugins-m3uiptv - 1.0+git344+d4b6880-r0.12 - enigma2-plugin-systemplugins-m3uiptv version 1.0+gitAUTOINC+d4b68807d2-r0
enigma2-plugin-systemplugins-m3uiptv-dbg - 1.0+git344+d4b6880-r0.12 - enigma2-plugin-systemplugins-m3uiptv version 1.0+gitAUTOINC+d4b68807d2-r0 - Debugging files
enigma2-plugin-systemplugins-m3uiptv-dev - 1.0+git344+d4b6880-r0.12 - enigma2-plugin-systemplugins-m3uiptv version 1.0+gitAUTOINC+d4b68807d2-r0 - Development files
enigma2-plugin-systemplugins-m3uiptv-src - 1.0+git344+d4b6880-r0.12 - enigma2-plugin-systemplugins-m3uiptv version 1.0+gitAUTOINC+d4b68807d2-r0 - Source files
iptvsubparser - 1.1+git8+e00b59f-r0.1 - iptvsubparser version 1.1+gitAUTOINC+e00b59f176-r0
iptvsubparser-dbg - 1.1+git8+e00b59f-r0.1 - iptvsubparser version 1.1+gitAUTOINC+e00b59f176-r0 - Debugging files
iptvsubparser-dev - 1.1+git8+e00b59f-r0.1 - iptvsubparser version 1.1+gitAUTOINC+e00b59f176-r0 - Development files
kodi-addon-pvr-iptvsimple - 20.6.0+git851+37b22be-r0.16 - Kodi Media Center PVR plugins
kodi-addon-pvr-iptvsimple-dbg - 20.6.0+git851+37b22be-r0.16 - Kodi Media Center PVR plugins - Debugging files
kodi-addon-pvr-iptvsimple-dev - 20.6.0+git851+37b22be-r0.16 - Kodi Media Center PVR plugins - Development files
root@vuultimo4k:~# opkg install enigma2-plugin-extensions-e2iplayer
 * opkg_prepare_url_for_install: Couldn't find anything to satisfy 'enigma2-plugin-extensions-e2iplayer'.
root@vuultimo4k:~# opkg install enigma2-plugin-extensions-e2iplayer
 * opkg_prepare_url_for_install: Couldn't find anything to satisfy 'enigma2-plugin-extensions-e2iplayer'.
root@vuultimo4k:~# cd/ var
-sh: cd/: not found
root@vuultimo4k:~# wget https://github.com/Blindspot76/e2iPlayer/archive/refs/he
ads/master.zip -O e2i.zip
--2025-08-26 06:36:30--  https://github.com/Blindspot76/e2iPlayer/archive/refs/heads/master.zip
Resolving github.com... 140.82.112.4
Connecting to github.com|140.82.112.4|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://codeload.github.com/Blindspot76/e2iPlayer/zip/refs/heads/master [following]
--2025-08-26 06:36:30--  https://codeload.github.com/Blindspot76/e2iPlayer/zip/refs/heads/master
Resolving codeload.github.com... 140.82.113.9
Connecting to codeload.github.com|140.82.113.9|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [application/zip]
Saving to: ‘e2i.zip’

e2i.zip                 [          <=>       ]  12.32M  6.19MB/s    in 2.0s    

2025-08-26 06:36:32 (6.19 MB/s) - ‘e2i.zip’ saved [12921533]

root@vuultimo4k:~# unzip e2i.zip
Archive:  e2i.zip
   creating: e2iPlayer-master/
   creating: e2iPlayer-master/IPTVPlayer/
  inflating: e2iPlayer-master/IPTVPlayer/.gitattributes
   creating: e2iPlayer-master/IPTVPlayer/Web/
  inflating: e2iPlayer-master/IPTVPlayer/Web/__init__.py
  inflating: e2iPlayer-master/IPTVPlayer/Web/__init__.pyo
  inflating: e2iPlayer-master/IPTVPlayer/Web/initiator.py
  inflating: e2iPlayer-master/IPTVPlayer/Web/initiator.pyo
   creating: e2iPlayer-master/IPTVPlayer/Web/locale/
.... more files ....
  inflating: e2iPlayer-master/IPTVPlayer/version.py
  inflating: e2iPlayer-master/README.md
  inflating: e2iPlayer-master/setup.py
  inflating: e2iPlayer-master/setup_translate.py
root@vuultimo4k:~# cp -r e2iPlayer-master/IPTVPlayer /usr/lib/enigma2/python/Plu
gins/Extensions/
root@vuultimo4k:~# chmod -R 755 /usr/lib/enigma2/python/Plugins/Extensions/IPTVP
layer
root@vuultimo4k:~# 