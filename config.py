import os

BASE_URL = os.getenv('STELLAR_BASE_URL', 'https://qa-stellarburgers.education-services.ru').rstrip('/')
WAIT_TIMEOUT = 20
ORDER_TIMEOUT = 40
