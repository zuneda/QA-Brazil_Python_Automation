import time

from selenium import webdriver

import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        options = webdriver.ChromeOptions()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(10)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        assert routes_page.get_from_location_value() == data.ADDRESS_FROM
        assert routes_page.get_to_location_value() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.select_comfort_tariff()

        print("função criada para selecionar plano")

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.select_comfort_tariff()
        time.sleep(2)
        routes_page.click_phone_number_button()
        time.sleep(2)
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        time.sleep(2)
        routes_page.click_next_button()
        time.sleep(2)
        code = helpers.retrieve_phone_code(self.driver)
        routes_page.enter_code(code)
        time.sleep(2)
        routes_page.click_confirm_button()
        time.sleep(2)
        assert data.PHONE_NUMBER in routes_page.get_phone_number_value()

        print("função criada para preencher telefone")

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        time.sleep(3)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        routes_page.click_call_taxi_button()
        time.sleep(2)
        routes_page.select_comfort_tariff()
        time.sleep(2)
        routes_page.click_payment_method_button()
        time.sleep(2)
        routes_page.click_add_card_button()
        time.sleep(2)
        routes_page.enter_card_number(data.CARD_NUMBER)
        time.sleep(3)
        routes_page.enter_card_code(data.CARD_CODE)
        time.sleep(3)
        routes_page.click_link_button()
        time.sleep(10)
        print("função criada para preencher cartão")

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(
            data.ADDRESS_FROM,
            data.ADDRESS_TO
        )
        routes_page.click_call_taxi_button()
        routes_page.select_comfort_tariff()
        time.sleep(2)
        routes_page.enter_message_for_driver(
            data.MESSAGE_FOR_DRIVER
        )
        time.sleep(5)
        assert (
                routes_page.get_message_for_driver_value()
                == data.MESSAGE_FOR_DRIVER
        )
        print("função criada para deixar comentário para motorista")

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.select_comfort_tariff()

        routes_page.order_blanket_and_handkerchiefs()
        time.sleep(5)

        print("função criada para pedir blanket e handkerchiefs")

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.select_comfort_tariff()

        for _ in range(2):
            routes_page.add_ice_cream()
        time.sleep(5)
        assert routes_page.get_ice_cream_count() == "2"

        print("função criada para pedir 2 sorvetes")

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.select_comfort_tariff()

        routes_page.click_order_taxi_button()
        time.sleep(5)

        print("função criada para procurar modelo do carro")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
