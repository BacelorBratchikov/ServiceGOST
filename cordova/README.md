# Cordova
Раздел отвечает за преобразование вёрстки в .apk

## Подготовка и запуск
*Для Windows*  
*Из директории ServiceGOST/cordova*
### 1. Установить плагины
```bash
$ cordova plugin add cordova-plugin-android-permissions
$ cordova plugin add cordova-plugin-file
$ cordova plugin add cordova-plugin-file-opener2
$ cordova plugin add cordova-plugin-file-transfer
$ cordova plugin add cordova-plugin-whitelist
```
### 2. Добавить Android в список экспортируемых платформ
```bash
$ cordova platform add android
```
### 3. Запустить преобразование
```bash
$ cordova build android
```
