import pytest
from selenium import webdriver
from data import *
from urban_routes_page import UrbanRoutesPage
from helpers import retrieve_phone_code
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    driver.get(URBAN_ROUTES_URL)
    yield driver
    driver.quit()

class TestUrbanRoutes:
    def test_enter_addresses(self, setup_driver):
        page = UrbanRoutesPage(setup_driver)
        page.enter_address(ADDRESS_FROM, ADDRESS_TO)
        assert setup_driver.find_element(*UrbanRoutesPage.ADDRESS_FROM_INPUT).get_attribute('value') == ADDRESS_FROM
        assert setup_driver.find_element(*UrbanRoutesPage.ADDRESS_TO_INPUT).get_attribute('value') == ADDRESS_TO

    def test_select_comfort_rate(self, setup_driver):
        page = UrbanRoutesPage(setup_driver)
        page.select_comfort_rate()
        assert setup_driver.find_element_by_class_name('tcard active').text == "Comfort"

    def test_enter_phone_number(self, setup_driver):
        page = UrbanRoutesPage(setup_driver)
        page.enter_phone_number(PHONE_NUMBER)
        code = retrieve_phone_code(setup_driver)
        assert code is not None

    def test_enter_card_details(self, setup_driver):
        page = UrbanRoutesPage(setup_driver)
        page.enter_card_details(CARD_NUMBER, CARD_CODE)
        assert "Tarjeta" in setup_driver.find_element_by_class_name('pp-value-text').text

