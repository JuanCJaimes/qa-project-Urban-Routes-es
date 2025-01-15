# urban_routes_page.py
from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_address(self, address):
        address_field = self.driver.find_element(By.ID, "from")
        address_field.send_keys(address)

    def select_comfort_tariff(self):
        comfort_option = self.driver.find_element(By.ID, "tarifa-comfort")
        comfort_option.click()

    def enter_phone_number(self, phone_number):
        phone_field = self.driver.find_element(By.ID, "phone-number")
        phone_field.send_keys(phone_number)

    def add_credit_card(self, card_number, card_code):
        self.driver.find_element(By.ID, "add-card").click()
        self.driver.find_element(By.ID, "card-number").send_keys(card_number)
        cvv_field = self.driver.find_element(By.CLASS_NAME, "card-input")
        cvv_field.send_keys(card_code)
        cvv_field.send_keys(Keys.TAB)
        self.driver.find_element(By.ID, "link").click()