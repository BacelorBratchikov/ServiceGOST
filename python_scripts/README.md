# Python Scripts
Раздел отвечает за парсинг с внешнего сервиса полного списка актуальных ГОСТ документов в Markdown формат

## Подготовка
*Для Windows*  
*Из директории ServiceGOST/python_scripts*
### Скачать и установить Python 3.8
при установке добавить "python" в переменную окружения "PATH", поставив соответствующую галочку
### Активировать виртуальное окружение
```bash
$ "venv/Scripts/activate.bat"
```
## Запуск
### 1. Собрать ссылки в .txt файлы
```bash
(venv)$ python parse_links.py
```
*Результат в gosts_solar.txt и gosts_wind.txt*
### 2. Собрать ГОСТ по каждой ссылке в JSON документы
```bash
(venv)$ python parse_each_gost.py
```
*Результат в gosts/*
### 3.1 Собрать Markdown шаблон страницы ГОСТ документа для всех JSON
```bash
(venv)$ python all_gost_md.py
```
*Результат в gost_mds/*
### 3.2 Собрать Markdown шаблоны категориальных списковых страниц для всех JSON
```bash
(venv)$ python all_gost_by_category.py
```
*Результат в wind/ и solar/*
## Завершение
### Деактивировать виртуальное окружение
```bash
$ "venv/Scripts/deactivate.bat"
```
