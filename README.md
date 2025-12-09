# Лабораторная работа: CI/CD Pipeline с GitHub Actions

![CI/CD Pipeline](https://github.com/Exxxto/lab6/actions/workflows/ci.yml/badge.svg)

## Описание проекта

Простое консольное приложение-калькулятор на Python для демонстрации настройки CI/CD pipeline в GitHub Actions.

## Функциональность

Калькулятор поддерживает следующие операции:
- Сложение
- Вычитание
- Умножение
- Деление
- Вычисление факториала

## Структура проекта

```
.
├── calculator.py                  # Основной код приложения
├── test_calculator.py             # Unit-тесты
├── requirements.txt               # Зависимости проекта
├── .github/
│   └── workflows/
│       └── ci.yml                 # Конфигурация GitHub Actions
├── .gitlab-ci.yml                 # Конфигурация GitLab CI (для справки)
└── README.md                      # Документация
```

## Демонстрация работы для преподавателя

### 1. Репозиторий на GitHub
Откройте: https://github.com/Exxxto/lab6

Покажите:
- Структуру проекта (файлы calculator.py, test_calculator.py, requirements.txt)
- Файл .github/workflows/ci.yml с конфигурацией pipeline
- Badge статуса CI/CD в README (зеленый badge = все работает)

### 2. Вкладка Actions
Откройте: https://github.com/Exxxto/lab6/actions

Покажите:
- Список запущенных workflows
- Успешное выполнение всех jobs (зеленые галочки)
- Кликните на последний workflow run и покажите:
  - Build and Setup
  - Run Tests (параллельно с Linting)
  - Code Quality Check (параллельно с Tests)
  - Security Scan
  - Pipeline Summary

### 3. Артефакты
В деталях workflow покажите раздел "Artifacts":
- coverage-report (отчет о покрытии кода)
- pylint-report (отчет о качестве кода)
- security-reports (отчет о безопасности)

### 4. Логи выполнения
Откройте любой job и покажите:
- Установку зависимостей
- Выполнение тестов
- Результаты проверок

## CI/CD Pipeline

Pipeline состоит из следующих jobs:

### 1. Build (Сборка)
- Установка Python 3.11 и зависимостей из requirements.txt
- Кэширование pip пакетов для ускорения последующих запусков
- Проверка синтаксиса Python файлов (py_compile)

### 2. Test (Тестирование) - выполняется параллельно с Linting

**Как работает:** Запускаются все unit-тесты из test_calculator.py двумя способами:
- pytest с измерением покрытия кода (coverage)
- unittest для дополнительной проверки

**Результат:** Генерируется HTML отчет о покрытии кода и XML файл. Отчеты сохраняются как артефакты на 7 дней. Если покрытие кода меньше ожидаемого, это видно в отчете.

### 3. Linting (Проверка качества кода) - выполняется параллельно с Test

**Как работает:** Инструмент pylint анализирует код на соответствие стандартам PEP 8 и выявляет:
- Ошибки стиля кода (отступы, пробелы, длина строк)
- Неиспользуемые переменные и импорты
- Потенциальные ошибки в логике
- Нарушения соглашений об именовании

**Результат:** Генерируется оценка качества кода (от 0 до 10). Минимальный порог установлен на 8.0. Отчет сохраняется в файл pylint-report.txt.

### 4. Security (Проверка безопасности)

**Как работает:** Два инструмента проверяют зависимости проекта:
- safety - сканирует requirements.txt и установленные пакеты на известные уязвимости из базы данных CVE
- pip-audit - дополнительная проверка через PyPI Advisory Database

**Результат:** Генерируются отчеты в JSON и текстовом формате со списком найденных уязвимостей, их серьезностью и рекомендациями по обновлению пакетов.

### 5. Notify (Уведомления) - выполняется при ошибках
- Отправка уведомлений в Slack (опционально)
- Комментарии в Pull Request при ошибках

### 6. Summary (Итоговый отчет)
- Генерация сводного отчета о выполнении pipeline с информацией о репозитории, ветке, коммите и авторе

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
pip-audit
```

## Настройка в GitHub

### 1. Создание репозитория

```bash
git init
git add .
git commit -m "Initial commit: Calculator with CI/CD"
git remote add origin https://github.com/Exxxto/lab6.git
git push -u origin main
```

### 2. Secrets (опционально)

В GitHub перейдите в Settings > Secrets and variables > Actions и добавьте:

- `SLACK_WEBHOOK_URL` - для уведомлений в Slack (если используете)

### 3. Просмотр результатов

После push в GitHub:
1. Перейдите во вкладку **Actions**
2. Выберите последний workflow run
3. Просмотрите результаты каждого job
4. Скачайте артефакты (отчеты о тестировании, линтинге, безопасности)

### 4. Badges

Badge статуса workflow уже добавлен в начало README:

```markdown
![CI/CD Pipeline](https://github.com/Exxxto/lab6/actions/workflows/ci.yml/badge.svg)
```

## Артефакты

Pipeline генерирует следующие артефакты:

- `coverage-report/` - HTML отчет о покрытии кода тестами
- `pylint-report.txt` - Отчет о качестве кода
- `security-reports/` - JSON и текстовые отчеты о уязвимостях

Артефакты доступны для скачивания в интерфейсе GitHub Actions в течение 7 дней.

## Настройка уведомлений в Slack

1. Создайте Incoming Webhook в вашем Slack workspace:
   - Перейдите в Slack App Directory
   - Найдите "Incoming WebHooks"
   - Добавьте в ваш канал
   - Скопируйте Webhook URL

2. Добавьте URL в GitHub:
   - Settings > Secrets and variables > Actions
   - New repository secret
   - Name: `SLACK_WEBHOOK_URL`
   - Value: вставьте ваш Webhook URL

3. Уведомления будут отправляться автоматически при ошибках в pipeline

## Интеграция с Codecov (опционально)

1. Зарегистрируйтесь на [codecov.io](https://codecov.io)
2. Подключите ваш GitHub репозиторий
3. Токен не требуется для публичных репозиториев
4. Для приватных репозиториев добавьте `CODECOV_TOKEN` в GitHub Secrets

## Используемые технологии

- **Python 3.11** - язык программирования
- **pytest** - фреймворк для тестирования
- **pylint** - инструмент статического анализа кода
- **safety** - проверка зависимостей на уязвимости
- **pip-audit** - дополнительная проверка безопасности
- **GitHub Actions** - платформа для автоматизации CI/CD
- **Codecov** - отслеживание покрытия кода (опционально)

## Сравнение GitLab CI/CD и GitHub Actions

| Аспект | GitLab CI/CD | GitHub Actions |
|--------|--------------|----------------|
| Конфигурация | `.gitlab-ci.yml` | `.github/workflows/*.yml` |
| Терминология | stages, jobs | jobs, steps |
| Runners | GitLab Runners | GitHub-hosted runners |
| Артефакты | artifacts | upload-artifact action |
| Кэширование | cache | cache action |
| Переменные | variables | env |
| Docker | Встроенная поддержка | Через actions |

Оба файла конфигурации (`.gitlab-ci.yml` и `.github/workflows/ci.yml`) включены в проект для сравнения.

## Критерии оценки

- Рабочий проект с минимальным функционалом и unit-тестами
- Правильно настроенный `.github/workflows/ci.yml` с jobs: build, test, linting, security
- Параллельное выполнение jobs test и linting
- Использование GitHub Actions runners (ubuntu-latest)
- Использование переменных окружения
- Кэширование зависимостей для ускорения pipeline
- Сохранение результатов в виде артефактов
- Настройка уведомлений об ошибках (опционально)
- Интеграция с Codecov для отслеживания покрытия (опционально)

## Автор

Студент направления 09.03.02 "Программное обеспечение для информационных систем"

## Лицензия

MIT
