# Используйте официальный образ Playwright
FROM mcr.microsoft.com/playwright:v1.45.0-jammy

# Установите Python и pip
RUN apt-get update && apt-get install -y python3.10 python3-pip

# Установите Playwright для Python
RUN python3.10 -m pip install --upgrade pip

# Копируйте requirements.txt и установите зависимости
COPY requirements.txt .
RUN python3.10 -m pip install --no-cache-dir -r requirements.txt

# Установите браузеры Playwright
RUN playwright install

# Установите рабочую директорию
WORKDIR /app

# Копируйте весь код в контейнер
COPY . .

# Команда запуска тестов с поддержкой переменных окружения
#CMD ["sh", "-c", "pytest ${PYTEST_ARGS}"]
CMD ["sh", "-c", "pytest ${PYTEST_ARGS:-tests}"]
