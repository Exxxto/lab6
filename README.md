## CI/CD Pipeline

Pipeline состоит из следующих этапов:

### 1. Build (Сборка)
- Создание виртуального окружения
- Установка зависимостей
- Проверка синтаксиса Python файлов

### 2. Test (Тестирование) - выполняется параллельно с Linting
- Запуск unit-тестов с помощью pytest
- Генерация отчета о покрытии кода
- Сохранение результатов в артефактах

### 3. Linting (Проверка качества кода) - выполняется параллельно с Test
- Статический анализ кода с помощью pylint
- Проверка соответствия стандартам PEP 8
- Генерация отчета о качестве кода

### 4. Security (Проверка безопасности)
- Сканирование зависимостей на известные уязвимости
- Использование инструмента safety
- Генерация отчета о безопасности

## Локальный запуск

### Установка зависимостей

```bash
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Запуск приложения

```bash
python calculator.py
```

### Запуск тестов

```bash
# С помощью pytest
pytest test_calculator.py -v

# С покрытием кода
pytest test_calculator.py -v --cov=calculator

# С помощью unittest
python -m unittest test_calculator.py -v
```

### Запуск линтера

```bash
pylint calculator.py test_calculator.py
```

### Проверка безопасности

```bash
safety check
```