# main.py
import pytest
from selenium import webdriver
from data import *
from urban_routes_page import UrbanRoutesPage
from helpers import retrieve_phone_code
from selenium.webdriver.common.by import By

@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    driver.get(URBAN_ROUTES_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_configurar_direccion(setup_driver):
    page = UrbanRoutesPage(setup_driver)
    page.enter_address(ADDRESS_FROM)
    assert setup_driver.find_element(By.ID, "from").get_attribute('value') == ADDRESS_FROM

def test_seleccionar_tarifa(setup_driver):
    page = UrbanRoutesPage(setup_driver)
    page.select_comfort_tariff()
    assert setup_driver.find_element(By.ID, "tarifa-comfort").is_selected()

def test_ingresar_numero(setup_driver):
    page = UrbanRoutesPage(setup_driver)
    page.enter_phone_number(PHONE_NUMBER)
    assert setup_driver.find_element(By.ID, "phone-input").get_attribute('value') == PHONE_NUMBER

def test_agregar_tarjeta_credito(setup_driver):
    page = UrbanRoutesPage(setup_driver)
    page.add_credit_card(CARD_NUMBER, CARD_CODE)
    # Simula la pérdida de foco para habilitar el botón de link
    setup_driver.find_element(By.TAG_NAME, "body").click()
    assert setup_driver.find_element(By.ID, "link").is_enabled()

def test_escribir_mensaje_conductor(setup_driver):
    page = UrbanRoutesPage(setup_driver)
    page.write_driver_message(MESSAGE_FOR_DRIVER)
    assert setup_driver.find_element(By.ID, "message").get_attribute('value') == MESSAGE_FOR_DRIVER

def test_pedir_manta_panuelos(setup_driver):
    page = UrbanRoutesPage(setup_driver)
    page.request_blanket_tissues()
    assert setup_driver.find_element(By.ID, "manta").is_selected()
    assert setup_driver.find_element(By.ID, "panuelos").is_selected()

def test_pedir_helados(setup_driver):
    page = UrbanRoutesPage(setup_driver)
    page.request_ice_cream(2)
    assert int(setup_driver.find_element(By.ID, "ice-cream-quantity").get_attribute('value')) == 2

def test_confirmar_modal_busqueda_taxi(setup_driver):
    page = UrbanRoutesPage(setup_driver)
    page.confirm_taxi_search_modal()
    assert setup_driver.find_element(By.ID, "taxi-modal").is_displayed()
