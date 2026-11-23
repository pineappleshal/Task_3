import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


class BrowserFactory:
    @staticmethod
    def create(browser, headless=True):
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument('--headless=new')
            if os.getenv('CHROME_BINARY'):
                options.binary_location = os.environ['CHROME_BINARY']
            service = ChromeService(executable_path=os.getenv('CHROMEDRIVER'))
            driver = webdriver.Chrome(service=service, options=options)
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument('-headless')
            if os.getenv('FIREFOX_BINARY'):
                options.binary_location = os.environ['FIREFOX_BINARY']
            service = FirefoxService(executable_path=os.getenv('GECKODRIVER'))
            driver = webdriver.Firefox(service=service, options=options)
        else:
            raise ValueError(f'Неизвестный браузер: {browser}')
        driver.set_window_size(1440, 1100)
        driver.set_page_load_timeout(40)
        return driver
