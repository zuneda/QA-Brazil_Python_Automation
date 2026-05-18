from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import webDriveWait
import time

class UrbanRoutesPage:
     # Secao DE e PARA
    from_field = By.Id ('from')
    to_field = By.Id('to')
     # driver e o google chrome
    def __init__(self,driver):
        # para ler o driver:
       self.driver = driver

        # criar a funcao do from element:
    def enter_from_location (self, from_text):
        # agora precisa ler os atributos:
     self.driver.find_element(*self.from_field).send_keys(from_text)

        # criar a funcao do to element:
    def enter_to_location (self, to_text):
        # agora precisa ler os atributos
     self.driver.find_element(*self.to_field).send_keys(to_text)

        # criar funcao para ler esses dois valores:
    def enter_locations (self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    #para pegar os valores:
    def get_to_location_value(self):
    #para prevenir nao ler campo vazio:
        return WebDriverWait(self.driver, timeout 3).until(EC.visibility_of_element_located(self.to_field)).get_attribute('value')

    


