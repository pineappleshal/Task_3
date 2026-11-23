# Task_3 — веб-тесты Stellar Burgers

17 сценариев выполняются в Google Chrome и Mozilla Firefox: всего 34 проверки.
Использованы Selenium, pytest, requests, Allure и Page Object Model.

## Запуск

```bash
python -m venv .venv
```

Windows: `.venv\Scripts\activate`. Linux/macOS: `source .venv/bin/activate`.

```bash
python -m pip install -r requirements.txt
python -m pytest --alluredir=allure-results --clean-alluredir
```

По умолчанию тесты запускаются в обоих браузерах без отображения окон.
Браузеры должны быть установлены, драйверы подбирает Selenium Manager.
Можно задать `CHROME_BINARY`, `FIREFOX_BINARY`, `CHROMEDRIVER`, `GECKODRIVER` для явных путей.

```bash
python -m pytest --browser=chrome
python -m pytest --browser=firefox --headed
allure serve allure-results
```

Готовый автономный отчёт: `allure-report/index.html`. Повторная генерация через Allure 3:

```bash
allure generate allure-results --config allurerc.json --output allure-report --clean
```

Стенд по умолчанию — `https://qa-stellarburgers.education-services.ru`.
Его можно заменить переменной окружения `STELLAR_BASE_URL` без завершающего `/api`.

## Сценарии

| Класс | Сценарии на один браузер |
| --- | --- |
| TestPasswordRecovery | Переход по ссылке восстановления; отправка почты; активация поля при показе пароля — 3 |
| TestAccount | Личный кабинет; история заказов; выход — 3 |
| TestConstructor | Переходы в конструктор и ленту; открытие и закрытие деталей ингредиента; увеличение счётчика; оформление заказа — 6 |
| TestFeed | Детали заказа; заказ из истории в общей ленте; увеличение общего и дневного счётчиков; номер заказа в работе — 5 |

## Устройство проекта

- `pages`: отдельный Page Object для каждой страницы. Работа с WebDriver и ожидания находятся в `BasePage`.
- `locators`: локаторы разделены по страницам.
- `helpers`: фабрика Chrome/Firefox и API для подготовки и удаления тестовых данных.
- `tests`: классы сгруппированы по функциональности.
- `conftest.py`: новый браузер и независимый API-пользователь для каждого нужного теста; скриншоты при ошибках.

Тесты не используют реальные аккаунты: пользователи с уникальными адресами example.com создаются через API и удаляются после проверки. Для восстановления используется только отправка запроса на тестовый email; настоящий пароль не сбрасывается. В API нет документированной ручки удаления заказа, поэтому после теста удаляется его владелец.

Для HTML5-перетаскивания React DnD передаются стандартные события с DataTransfer через Selenium. Состояние приложения напрямую не изменяется. Вместо фиксированных пауз используются явные ожидания; повторный поиск элементов учитывает обновления WebSocket и анимацию модальных окон.

Счётчики заказов проверяются на увеличение, а не строго на +1: учебный стенд общий, параллельно на нём работают другие пользователи. В тестах также проверяется появление номера именно созданного заказа.

Рабочая ветка: `develop3`.
