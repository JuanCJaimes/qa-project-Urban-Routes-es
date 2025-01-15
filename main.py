# main.py
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

def test_configurar_direccion(setup_driver):
    page = UrbanRoutesPage(setup_driver)
    page.enter_address(ADDRESS_FROM)
    assert setup_driver.find_element("id", "from").get_attribute('value') == ADDRESS_FROM

def test_seleccionar_tarifa(setup_driver):
    page = UrbanRoutesPage(setup_driver)
    page.select_comfort_tariff()
    assert setup_driver.find_element("id", "tarifa-comfort").is_selected()

def test_ingresar_numero(setup_driver):
    page = UrbanRoutesPage(setup_driver)
    page.enter_phone_number(PHONE_NUMBER)
    assert setup_driver.find_element("id", "phone-number").get_attribute('value') == PHONE_NUMBER

def test_agregar_tarjeta_credito(setup_driver):
    page = UrbanRoutesPage(setup_driver)
    page.add_credit_card(CARD_NUMBER, CARD_CODE)
    confirmation_code = retrieve_phone_code(setup_driver)
    assert confirmation_code == '1234'
