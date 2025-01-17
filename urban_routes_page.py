from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    # Localizadores declarados al inicio
    ADDRESS_FROM_INPUT = (By.ID, 'from')
    ADDRESS_TO_INPUT = (By.ID, 'to')
    COMFORT_RATE_BUTTON = (By.XPATH, '//div[@class="tcard"]//div[contains(text(), "Comfort")]')
    PHONE_MODAL_TRIGGER = (By.CLASS_NAME, 'phone-modal-trigger')
    PHONE_CONFIRM_BUTTON = (By.CLASS_NAME, 'phone-confirm')
    CARD_MODAL_TRIGGER = (By.CLASS_NAME, 'payment-method-trigger')
    ADD_CARD_BUTTON = (By.CLASS_NAME, 'add-card')
    CARD_NUMBER_INPUT = (By.CLASS_NAME, 'card-number')
    CARD_CVV_INPUT = (By.CLASS_NAME, 'card-cvv')
    CARD_SUBMIT_BUTTON = (By.CLASS_NAME, 'submit-card')
    BLANKET_TISSUE_CHECKBOX = (By.ID, 'blanket-tissue')
    ICE_CREAM_QUANTITY_INPUT = (By.ID, 'ice-cream-quantity')
    TAXI_MODAL = (By.CLASS_NAME, 'taxi-modal')

    def __init__(self, driver):
        self.driver = driver

    def enter_address(self, from_address, to_address):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.ADDRESS_FROM_INPUT))
        self.driver.find_element(*self.ADDRESS_FROM_INPUT).send_keys(from_address)
        self.driver.find_element(*self.ADDRESS_TO_INPUT).send_keys(to_address)

    def select_comfort_rate(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.COMFORT_RATE_BUTTON)).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_MODAL_TRIGGER).click()
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.PHONE_CONFIRM_BUTTON)).click()

    def enter_card_details(self, card_number, cvv):
        self.driver.find_element(*self.CARD_MODAL_TRIGGER).click()
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.ADD_CARD_BUTTON)).click()
        self.driver.find_element(*self.CARD_NUMBER_INPUT).send_keys(card_number)
        self.driver.find_element(*self.CARD_CVV_INPUT).send_keys(cvv)
        self.driver.find_element(*self.CARD_SUBMIT_BUTTON).click()

    def request_blanket_tissues(self):
        self.driver.find_element(*self.BLANKET_TISSUE_CHECKBOX).click()

    def request_ice_cream(self, quantity):
        ice_cream_input = self.driver.find_element(*self.ICE_CREAM_QUANTITY_INPUT)
        ice_cream_input.clear()
        ice_cream_input.send_keys(quantity)

    def confirm_taxi_search_modal(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.TAXI_MODAL))