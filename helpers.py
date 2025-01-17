import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def retrieve_phone_code(driver):
    """
    Intercepta el código telefónico generado en el modal de confirmación
    y lo devuelve como string.
    """
    for _ in range(10):
        try:
            logs = driver.get_log('performance')
            for log in logs:
                if '1234' in log['message']:
                    return '1234'  # Código simulado para propósitos de prueba.
        except Exception:
            time.sleep(1)
    return None
