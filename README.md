# effective-mobile-autotests
#Скачать python версии 3.10 https://www.python.org/downloads/release/python-3100/

Автоматизация тестирования главной страницы сайта effective-mobile.ru
Этот проект предназначен для автоматизированного UI-тестирования главной страницы сайта effective-mobile.ru 
с использованием Playwright и Python 3.10. 
Проект реализован с применением паттерна Page Object Model (POM) 
и интегрирован с Allure для генерации отчетов.

Быстрый старт (локальный запуск)
1. Клонируйте репозиторий
git clone <ваш_репозиторий>
cd <ваш_проект>

2. Создайте виртуальное окружение
python3.10 -m venv venv
source venv/bin/activate  # Linux/macOS
# или
venv\Scripts\activate     # Windows

3. Установите зависимости
pip install -r requirements.txt

4. Установите браузеры для Playwright
playwright install

5. Запустите тесты
pytest

6. Сгенерируйте отчет Allure (опционально)
allure serve ./allure-results

Запуск через Docker
1. Соберите и запустите контейнер
docker-compose up --build

Все отчеты будут сохранены в папке ./allure-results.

2. Просмотр отчетов Allure (локально)
allure serve ./allure-results


Ссылка на репозиторий - https://github.com/Stasss1985/effective-mobile-autotests

Автор
Кривко Станислав Юрьевич - https://github.com/Stasss1985?tab=repositories