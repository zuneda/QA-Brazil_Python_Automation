import data
import helpers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import webDriveWait
import time

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print ("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
    #teste automatizado precisa de uma assertiva ( garantir que foi escrito o nome correto)
        assert routes_page.get_from_location_value()== data.ADDRESS_FROM
        assert routes_page.get_to_location_value() == data.ADDRESS_TO
        


    def test_select_plan(self):
        # Dictionary em S8
        print("função criada para selecionar plano")
        pass

    def test_fill_phone_number(self):
        # Dictionary em S8
        print("função criada para preencher telefone")
        pass

    def test_fill_phone_number(self):
        # Dictionary em S8
        print("função criada para preencher telefone")
        pass

    def test_fill_card(self):
        # Dictionary em S8
        print("função criada para preencher cartao")
        pass

    def test_comment_for_driver(self):
        # Dictionary em S8
        print("função criada para deicar comentario motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Dictionary em S8
        print("função criada para pedir blanket e handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # Dictionary em S8
        numbers_of_ice_creams = 2
        for count in range(numbers_of_ice_creams):
         print("função criada para pedir 2 sorvetes")
        pass

    def test_car_search_model_appears(self):
        # Dictionary em S8
        print("função criada para procurar modelo do carro")
        pass
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

