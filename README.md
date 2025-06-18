# 📈 CSV Processor CLI Tool

Утилита командной строки для простого анализа CSV-файлов: фильтрация и агрегация по колонкам с выводом результата в виде красивой таблицы.

---

## 🚀 Возможности

- 🔍 **Фильтрация** по одной колонке с операторами: `=`, `<`, `>`, `<=`, `>=`
- 🧮 **Агрегация** по числовым колонкам: `avg` (среднее), `min` (минимум), `max` (максимум)
- 📊 Вывод результатов в виде таблицы с помощью `tabulate`
- ✅ Простое использование через аргументы CLI

---

## 🛠️ Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/sergeiBogdano/csv_prosesor.git
cd csv_prosesor
```

2. Создайте виртуальное окружение и активируйте его:

# Windows PowerShell
python -m venv .venv
.venv\Scripts\activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Использование

### ▶️ Базовый запуск

```bash
python main.py --file products.csv
```

### 🔎 Фильтрация

Укажите `--filter` с условием:

```bash
python main.py --file products.csv --filter "price>300"
python main.py --file products.csv --filter "brand=xiaomi"
```

Поддерживаемые операторы: `=`, `<`, `>`, `<=`, `>=`

### 📐 Агрегация

Укажите `--aggregate` с операцией:

```bash
python main.py --file products.csv --aggregate "price=avg"
python main.py --file products.csv --aggregate "rating=max"
```

Поддерживаются агрегаторы: `avg`, `min`, `max`

### 🧩 Комбинированный запрос

```bash
python main.py --file products.csv --filter "brand=xiaomi" --aggregate "price=max"
```

---

## 🧪 Тестирование

Запуск unit-тестов:

```bash
pytest
```

---

## 🗂️ Структура проекта

```text
csv_prosesor/
│
├── processor/
│   ├── aggregator.py      # Агрегация
│   ├── filter.py          # Фильтрация
│   ├── formatter.py             # Парсинг аргументов
│   └── loader.py          # Загрузка CSV
│
├── tests/
│
│
├── main.py                # Точка входа
├── requirements.txt
└── README.md
```

---

## 📎 Требования

- Python 3.7+
- `tabulate` — для форматированного вывода
- `pytest`, `pytest-cov` — для тестирования

---
