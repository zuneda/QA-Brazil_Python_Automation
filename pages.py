from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class UrbanRoutesPage:
    # Seção DE e PARA
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Botão para pedir táxi
    call_taxi_button = (By.XPATH, '//button[contains(text(), "Chamar um táxi")]')

    # Tarifa Comfort
    comfort_tariff = (By.XPATH, '//div[contains(text(), "Comfort")]')

    # Telefone
    phone_number_button = (By.CLASS_NAME, 'np-button')
    phone_number_field = (By.ID, 'phone')
    next_button = (By.XPATH, '//button[contains(text(), "Próximo")]')
    code_field = (By.ID, 'code')
    confirm_button = (By.XPATH, '//button[contains(text(), "Confirmar")]')

    # Pagamento
    payment_method_button = (By.CLASS_NAME,'pp-button')
    add_card_button = (By.XPATH,'//div[contains(text(), "Adicionar cartão")]')
    card_number_field = (By.NAME, 'number')
    card_code_field = (By.NAME, 'code')
    link_button = (By.XPATH,'//button[text()="Adicionar"]')
    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        self.driver.find_element(*self.from_field).send_keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.to_field).send_keys(to_text)

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def get_from_location_value(self):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.from_field)
        ).get_attribute('value')

    def get_to_location_value(self):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.to_field)
        ).get_attribute('value')

    def click_call_taxi_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.call_taxi_button)
        ).click()

    def select_comfort_tariff(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.comfort_tariff)
        ).click()

    def click_phone_number_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.phone_number_button)
        ).click()

    def enter_phone_number(self, phone_number):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.phone_number_field)
        ).send_keys(phone_number)

    def get_phone_number_value(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.phone_number_button)
        ).text

    def click_next_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.next_button)
        ).click()

    def enter_code(self, code):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.code_field)
        ).send_keys(code)

    def click_confirm_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.confirm_button)
        ).click()

    def click_payment_method_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.payment_method_button)
        ).click()

    def click_add_card_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.add_card_button)
        ).click()

    def enter_card_number(self, card_number):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.card_number_field)
        ).send_keys(card_number)

    def enter_card_code(self, card_code):
        field = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.card_code_field)
        )
        field.send_keys(card_code)
        field.send_keys(Keys.TAB)

    def click_link_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.link_button)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            button
        )
        self.driver.execute_script(
            "arguments[0].click();",
            button
        )


