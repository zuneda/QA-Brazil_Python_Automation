import data
import helpers

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
        # Dictionary em S8
        print("função criada para definir a rota")
        pass

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

