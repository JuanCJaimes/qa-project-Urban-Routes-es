from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    # Localizadores
    ADDRESS_FROM_INPUT = (By.ID, 'from')
    ADDRESS_TO_INPUT = (By.ID, 'to')
    COMFORT_RATE_BUTTON = (By.XPATH, '//div[@class="tcard"]//div[contains(text(), "Comfort")]')
    PHONE_FIELD = (By.CSS_SELECTOR, '.phone-input')
    CARD_NUMBER_INPUT = (By.CSS_SELECTOR, '.card-number')
    CVV_INPUT = (By.CSS_SELECTOR, '.card-cvv')
    DRIVER_MESSAGE_INPUT = (By.CSS_SELECTOR, '#message')
    BLANKET_TISSUE_CHECKBOX = (By.CSS_SELECTOR, '.checkbox-blanket-tissue')
    ICE_CREAM_QUANTITY_INPUT = (By.CSS_SELECTOR, '.ice-cream-quantity')
    TAXI_MODAL = (By.CSS_SELECTOR, '.taxi-modal')

    def __init__(self, driver):
        self.driver = driver

    def enter_address(self, from_address, to_address):
        self.driver.find_element(*self.ADDRESS_FROM_INPUT).send_keys(from_address)
        self.driver.find_element(*self.ADDRESS_TO_INPUT).send_keys(to_address)

    def select_comfort_rate(self):
        self.driver.find_element(*self.COMFORT_RATE_BUTTON).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone_number)

    def enter_card_details(self, card_number, cvv):
        self.driver.find_element(*self.CARD_NUMBER_INPUT).send_keys(card_number)
        self.driver.find_element(*self.CVV_INPUT).send_keys(cvv)

    def write_driver_message(self, message):
        self.driver.find_element(*self.DRIVER_MESSAGE_INPUT).send_keys(message)

    def request_blanket_and_tissue(self):
        self.driver.find_element(*self.BLANKET_TISSUE_CHECKBOX).click()

    def request_ice_cream(self, quantity):
        self.driver.find_element(*self.ICE_CREAM_QUANTITY_INPUT).send_keys(quantity)

    def confirm_taxi_modal(self):
        return self.driver.find_element(*self.TAXI_MODAL).is_displayed()
