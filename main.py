from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_order_taxi():
    # Inicializar el navegador
    driver = webdriver.Chrome()
    driver.get("https://url-del-sitio-web.com")

    # 1. Configurar la dirección
    address_field = driver.find_element(By.ID, "address-input")
    address_field.send_keys("Calle 123, Ciudad")
    address_field.send_keys(Keys.RETURN)

    # 2. Seleccionar tarifa Comfort
    comfort_option = driver.find_element(By.ID, "tarifa-comfort")
    comfort_option.click()

    # 3. Rellenar el número de teléfono
    phone_input = driver.find_element(By.ID, "phone-input")
    phone_input.send_keys("1234567890")
    phone_input.send_keys(Keys.RETURN)

    # 4. Agregar tarjeta de crédito
    card_button = driver.find_element(By.ID, "add-card-button")
    card_button.click()

    # Rellenar formulario de tarjeta
    card_number_input = driver.find_element(By.ID, "card-number")
    card_number_input.send_keys("4111111111111111")

    cvv_input = driver.find_element(By.ID, "cvv")
    cvv_input.send_keys("123")
    cvv_input.send_keys(Keys.TAB)  # Cambia el foco para activar el botón 'link'

    link_button = driver.find_element(By.ID, "code")
    link_button.click()

    # 5. Escribir mensaje al conductor
    driver.find_element(By.ID, "driver-message").send_keys("Por favor, conduzca con cuidado.")

    # 6. Pedir manta y pañuelos
    driver.find_element(By.ID, "request-blanket").click()
    driver.find_element(By.ID, "request-tissues").click()

    # 7. Pedir 2 helados
    ice_cream_input = driver.find_element(By.ID, "ice-cream-quantity")
    ice_cream_input.clear()
    ice_cream_input.send_keys("2")

    # 8. Confirmar pedido
    confirm_button = driver.find_element(By.ID, "confirm-order")
    confirm_button.click()

    # 9. Esperar la confirmación del taxi
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "driver-info"))
    )

    # 10. Validar confirmación
    assert driver.find_element(By.ID, "driver-info").is_displayed()

    driver.quit()
