if exist _site rmdir /s /q _site
if exist obj rmdir /s /q obj
if exist api rmdir /s /q api

C:\Programs\docfx\docfx.exe docfx.json --build