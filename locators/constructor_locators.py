from selenium.webdriver.common.by import By


class ConstructorLocators:
    TITLE = (By.XPATH, '//h1[text()="Соберите бургер"]')
    FIRST_BUN = (By.XPATH, '(//h2[text()="Булки"]/following-sibling::ul[1]/a)[1]')
    FIRST_SAUCE = (By.XPATH, '(//h2[text()="Соусы"]/following-sibling::ul[1]/a)[1]')
    BUN_NAME = (By.XPATH, '(//h2[text()="Булки"]/following-sibling::ul[1]/a)[1]/p')
    BUN_COUNTER = (By.XPATH, '(//h2[text()="Булки"]/following-sibling::ul[1]/a)[1]//p[contains(@class,"counter_counter__num")]')
    SAUCE_COUNTER = (By.XPATH, '(//h2[text()="Соусы"]/following-sibling::ul[1]/a)[1]//p[contains(@class,"counter_counter__num")]')
    BASKET = (By.CSS_SELECTOR, 'section[class*="BurgerConstructor_basket__"]')
    PLACE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')
    INGREDIENT_TITLE = (By.XPATH, '//section[contains(@class,"Modal_modal_opened")]//h2[text()="Детали ингредиента"]')
    INGREDIENT_NAME = (By.CSS_SELECTOR, '[class*="Modal_modal_opened"] p.text_type_main-medium')
    ORDER_NUMBER = (By.CSS_SELECTOR, '[class*="Modal_modal_opened"] h2')
    ORDER_CONFIRMATION = (By.XPATH, '//*[contains(@class,"Modal_modal_opened")]//p[text()="Ваш заказ начали готовить"]')
