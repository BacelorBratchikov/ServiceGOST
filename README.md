# ServiceGOST
 Android приложение для каталогизации и чтения ГОСТ документов в области ветро и гелео энергетики.

## Демо использования
<img src="samples\demo.gif" width="250px"/>

## Разделы
* `python_scripts` - Парсинг ГОСТ документов в Markdown файлы [↩](/python_scripts)
* `docfx` - Преобразование Markdown файлов в HTML верстку на базе DocFX [↩](/docfx)
* `cordova` - Преобразование верстки в Android приложение [↩](/cordova)

## Как установить
*Из директории ServiceGost*
### 1. Склонировать репозиторий
```bash
$ git clone https://github.com/bakalavrbrat/ServiceGOST.git  
```
### 2. [Выполнить парсинг ГОСТ документов](/python_scripts/README.md)
### 3. Экспортировать получившиеся Markdown в DocFX
Перенести только содержимое папок python_scripts/wind/, python_scripts/solar/, python_scripts/gost_mds/ в папки docfx/wind/, docfx/solar/, docfx/gost_mds/ соответственно с заменой
### 4. [Собрать верстку](/docfx/README.md)
Перенести только содержимое папок docfx/_site/wind/, docfx/_site/solar/, docfx/_site/gost_mds/ в папки cordova/www/wind/, cordova/www/solar/, cordova/www/gost_mds/ соответственно с заменой
### 5. [Собрать .apk](/cordova/README.md)

## Как запустить
*Из директории ServiceGost*
### Через телефон
Подключить устройство по USB, удостовериться, что на нем включен режим отладки по USB в настрйоках разработчика
### Через эмулятор
Установить и запустить эмулятор (желательно через AndroidStudio), запустить его через AVD Manager в AndroidStudio
### Запуск встроеного run.bat
```bash
$ cd cordova && platforms\android\cordova\run.bat  
```
