# helpers.py
import time
from selenium.webdriver.common.by import By

def retrieve_phone_code(driver):
    """Intercepta el código telefónico generado."""
    for _ in range(10):
        try:
            logs = driver.get_log('performance')
            for log in logs:
                if '1234' in log['message']:
                    return '1234'
        except:
            time.sleep(1)
    return None
