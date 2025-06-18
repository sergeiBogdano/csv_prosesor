CSV Processor CLI Tool
Утилита для простого и удобного анализа CSV-файлов из командной строки с поддержкой фильтрации и агрегации.

Описание
Скрипт загружает CSV-файл и позволяет:

Фильтровать данные по одной колонке с операторами: =, <, >, <=, >=

Выполнять агрегацию (среднее, минимум, максимум) по числовой колонке

Выводить данные и результаты агрегации в удобной таблице в консоли

Установка
Клонировать репозиторий:

bash
Копировать
Редактировать
git clone <URL_репозитория>
cd csv_processor
Создать и активировать виртуальное окружение:

bash
Копировать
Редактировать
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
.venv\Scripts\activate     # Windows PowerShell
Установить зависимости:

bash
Копировать
Редактировать
pip install -r requirements.txt
Использование
Запуск скрипта с обязательным указанием файла:

bash
Копировать
Редактировать
python main.py --file path/to/file.csv
Фильтрация
Передать параметр --filter в формате:

sql
Копировать
Редактировать
column=значение
column>значение
column<значение
column>=значение
column<=значение
Пример:

bash
Копировать
Редактировать
python main.py --file products.csv --filter "price>300"
Агрегация
Передать параметр --aggregate в формате:

ini
Копировать
Редактировать
column=операция
где операция — одна из: avg, min, max

Пример:

bash
Копировать
Редактировать
python main.py --file products.csv --aggregate "rating=avg"
Совместное использование
Сначала фильтрация, затем агрегация:

bash
Копировать
Редактировать
python main.py --file products.csv --filter "brand=xiaomi" --aggregate "price=max"
Пример вывода
pgsql
Копировать
Редактировать
+---------------+---------+---------+----------+
| name          | brand   |   price |   rating |
+===============+=========+=========+==========+
| redmi note 12 | xiaomi  |     199 |    4.600 |
+---------------+---------+---------+----------+
| poco x5 pro   | xiaomi  |     299 |    4.400 |
+---------------+---------+---------+----------+

📊 Результат агрегации: MAX по 'price' = 299
Тестирование
Запуск тестов с помощью pytest:

bash
Копировать
Редактировать
pytest
Для проверки покрытия кода:

bash
Копировать
Редактировать
pytest --cov=core tests/
Структура проекта
css
Копировать
Редактировать
csv_processor/
│
├── core/
│   ├── aggregator.py
│   ├── filter.py
│   ├── formatter.py
│   └── loader.py
│
├── tests/
│   ├── test_aggregator.py
│   ├── test_filter.py
│   └── ...
│
├── main.py
├── requirements.txt
└── README.md
Требования
Python 3.7+

tabulate

pytest (для тестирования)

