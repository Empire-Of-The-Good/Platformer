# Platformer

<div align="center">

<img src="assets/logo.png" alt="Logo" width="400">

**Динамичный 2D-платформер с кучей уровней, монеток и скрытых отсылок!**

[![Version 1.0.0](https://img.shields.io/badge/version-0.1.0--dev-red.svg)](https://github.com/python3demon/Platformer)
[![Python 3.14](https://img.shields.io/badge/python-3.14-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/latest/python3.14/)
[![Pygame 2.6.1](https://img.shields.io/badge/pygame-2.6.1-yellow.svg)](https://www.pygame.org/)
[![Linux](https://img.shields.io/badge/platform-linux-A9A9A9.svg?logo=linux&logoColor=white)](https://linux.org)
[![Windows](https://img.shields.io/badge/platform-windows-A9A9A9.svg?logo=windows&logoColor=white)](https://www.microsoft.com/ru-ru/software-download/windows11)

</div>


## Об игре
**Platformer Game** — это классический 2D-платформер на движке Pygame, где вам предстоит пройти сквозь огонь, воду и **67 хардкорных уровней**. Здесь нет заумного лора или драматичного сюжета — только чистый кайф, смешная атмосфера и тонны скрытых пасхалок для внимательных игроков!

* **Четкий расчет**: Прыгайте ровно на высоту в 2 блока. Никаких заносов и скольжений, управление отзывчивое как швейцарские часы!
* **Лазерное шоу**: Враги думали, что вы будете прыгать им на головы? Ха! Выжигайте их издалека мощным лазером.
* **Внутриигровая экономика**: Собирайте монетки на картах и получайте бонусы за прохождение.
* **Магазин скинов**: Тратьте честно заработанное золото на покупку уникальных образов. Соберете их все — увидите секретный финал!

> [!IMPORTANT]
> **Пока многое не сделано и находится в разработке!**

### Управление

* `A` / `D` — Движение влево / вправо (медленно, но уверенно)
* `W` — Прыжок (высота — ровно 2 блока, полный контроль в воздухе!)
* `LMB` (Левая кнопка мыши) / `F` — Огонь лазером издалека

## Installation & Launch (For Users)

### Windows
Убедитесь, что у вас установлен [Python 3.14](https://www.python.org/downloads/latest/python3.14/)

1. Скачайте репозиторий архивом и распакуйте его на компьютер.
2. Зайдите в папку `install\Windows`.
3. Дважды кликните по файлу `install.bat`. 
4. Скрипт сам установит все зависимости и скомпилирует исходный код в исполняемый `.exe` файл. Игру можно будет найти и запустить в появившейся папке `Platformer`.

> [!WARNING]
> **Важное примечание:** Не перемещайте файлы по отдельности. Перемещайте игру целиком, перенося всю папку `Platformer`.
---

## 💻 Installation & Launch (For Programmers)

### Linux
```bash
# Клонируем репозиторий и переходим в папку проекта
git clone https://github.com/python3demon/Platformer.git
cd Platformer

# Создаем и активируем виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# Устанавливаем зависимости
pip3 install -r requirements.txt

# Запуск игры
python3 main.py
```

### Windows
Для быстрой автоматической настройки вы можете просто запустить готовый файл `install.bat` из папки `install\Windows`, либо выполнить команды ручной настройки ниже.

```cmd
:: Клонируем репозиторий и переходим в папку проекта
git clone https://github.com/python3demon/Platformer.git
cd Platformer

:: Создаем и активируем виртуальное окружение
python -m venv venv
call venv\Scripts\activate.bat

:: Устанавливаем зависимости
pip install -r requirements.txt

:: Запуск игры из исходного кода
python main.py
```
Если же нужен готовый один .exe файл без консоли:
```cmd
pyinstaller --noconfirm --onefile --windowed --name "Platformer" main.py
```
Игра будет лежать **в папке `dist`**.

## Стек технологий
* **Language:** Python 3.14+
* **Library:** Pygame CE 2.6.1+
* **Environment:** Virtualenv

