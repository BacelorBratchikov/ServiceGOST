if exist _site rmdir /s /q _site
if exist obj rmdir /s /q obj
if exist api rmdir /s /q api

C:\Users\RUGyron\Documents\GitHub\ServiceGOST\docfx\docfx.exe docfx.json --serve   -p 8081