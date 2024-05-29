# Установка и запуск

Создаем виртуальное окружение

```bash
python -m venv venv
```

Активируем виртуальное окружение.
На Unix системах:
```bash
source venv/bin/activate
```
или на Windows:
```bash
venv\Scripts\activate.bat
```

Устанавливаем зависимости
```bash
pip install -r requirements.txt
```

Создаем файл с переменными окружения `.env` и добавляем туда токен из BotFather для бота
```
BOT_TOKEN=42:TOKEN
```

Запускаем бота:
```bash
python bot.py
```
