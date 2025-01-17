import pytest
from selenium import webdriver
from data import *
from urban_routes_page import UrbanRoutesPage
from helpers import retrieve_phone_code

@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    driver.get(URBAN_ROUTES_URL)
    yield driver
    driver.quit()

class TestUrbanRoutes:
    def test_enter_address(self, setup_driver):
        page = UrbanRoutesPage(setup_driver)
        page.enter_address(ADDRESS_FROM, ADDRESS_TO)
        assert setup_driver.find_element_by_id('from').get_attribute('value') == ADDRESS_FROM

    def test_select_comfort_rate(self, setup_driver):
        page = UrbanRoutesPage(setup_driver)
        page.select_comfort_rate()
        assert "Comfort" in setup_driver.find_element_by_class_name('tcard active').text

    def test_enter_phone_number(self, setup_driver):
        page = UrbanRoutesPage(setup_driver)
        page.enter_phone_number(PHONE_NUMBER)
        code = retrieve_phone_code(setup_driver)
        assert code is not None

    def test_enter_card_details(self, setup_driver):
        page = UrbanRoutesPage(setup_driver)
        page.enter_card_details(CARD_NUMBER, CARD_CODE)
        assert "Tarjeta" in setup_driver.find_element_by_class_name('pp-value-text').text

    def test_send_driver_message(self, setup_driver):
        page = UrbanRoutesPage(setup_driver)
        page.write_driver_message(MESSAGE_FOR_DRIVER)
        assert setup_driver.find_element_by_class_name('message-box').text == MESSAGE_FOR_DRIVER

    def test_request_blanket_tissues(self, setup_driver):
        page = UrbanRoutesPage(setup_driver)
        page.request_blanket_tissues()
        assert setup_driver.find_element_by_id('blanket-tissue').is_selected()

    def test_request_ice_cream(self, setup_driver):
        page = UrbanRoutesPage(setup_driver)
        page.request_ice_cream(2)
        assert int(setup_driver.find_element_by_id('ice-cream-quantity').get_attribute('value')) == 2

    def test_confirm_taxi_modal(self, setup_driver):
        page = UrbanRoutesPage(setup_driver)
        page.confirm_taxi_search_modal()
        assert setup_driver.find_element_by_class_name('taxi-modal').is_displayed()