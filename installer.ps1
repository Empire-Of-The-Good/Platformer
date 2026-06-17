$GameName = "Platformer"
$RootPath = "$PSScriptRoot\.." # Корневая папка где лежит исходный код проекта
$path_exe = "$PSScriptRoot\$GameName" # Путь будет лежать готовый exe-шник

Write-Host ("="*29)
Write-Host ("="*10) -NoNewline
Write-Host INSTALLER -ForegroundColor Green -NoNewline
Write-Host ("="*10)
Write-Host ("="*29)

if (-not $(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Пайтон не установлен!" -ForegroundColor Red
    Write-Host "Установите его по инструкции https://metanit.com/python/tutorial/1.2.php."
    Read-Host "Для продолжения нажмите клавишу Enter..."
    exit
}

if (-not (Test-Path "$RootPath\venv" -PathType Container)) {
    Write-Host "Создание виртуального окружения..."
    python -m venv "$RootPath\venv"
}

# Проверка наличия библиотек по очереди из файла requirements.txt в корневой папке
Write-Host "Активация виртуального окружения"
& "$RootPath\venv\Scripts\Activate.ps1"
foreach ($line in Get-Content "$RootPath\requirements.txt") {
    if ($line.Trim().Length -eq 0) { continue }
    $pkg_name = $line -replace "[<>=].*", ""
    Write-Host "Проверка наличия библиотеки $pkg_name..."

    pip show $pkg_name *> $null
    if ($LastExitCode -ne 0) {
        Write-Host "Установка библиотеки $pkg_name..." -ForegroundColor Cyan
        pip install $line *> $null
    } else {
        Write-Host "Библиотека $pkg_name уже установлена" -ForegroundColor Cyan

    }
}

Write-Host "Создание папки для игры..."
New-Item -ItemType Directory -Path "$path_exe" -Force > $null
New-Item -ItemType Directory -Path "$path_exe\assets" -Force > $null

Write-Host "Сборка из исходников в .EXE..." -ForegroundColor Cyan
pyinstaller --noconfirm --onedir --windowed --name "$GameName" --distpath "$PSScriptRoot" "$RootPath\main.py" > $null
if ($LastExitCode -ne 0) {
    Write-Host "Произошла ошибка в процессе компиляции." -ForegroundColor Red
    Read-Host "Для продолжения нажмите клавишу Enter..."
    exit
}

Write-Host "Копирование ресурсов игры..."
# Принудительно перезаписывает конфиги и assets (через флаг -Force)
Copy-Item -Path "$RootPath\assets" -Destination "$path_exe\assets" -Recurse -Force
Copy-Item -Path "$RootPath\*.json" -Destination "$path_exe" -Force

Write-Host "Компиляция успешно завершена!" -ForegroundColor Green
Write-Host "Игра лежит по пути: `"$path_exe`""
    Read-Host "Для продолжения нажмите клавишу Enter..."