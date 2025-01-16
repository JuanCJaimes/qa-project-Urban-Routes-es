# helpers.py

import time
from selenium.common.exceptions import WebDriverException

def retrieve_phone_code(driver) -> str:
    """
    Intercepta el código telefónico generado y lo devuelve como un string.

    Este código de confirmación se obtiene de los logs generados por el navegador.
    Intenta interceptar el código hasta un máximo de 10 veces antes de fallar.
    """
    for _ in range(10):  # Intentar un máximo de 10 veces
        try:
            # Obtener los logs de rendimiento del navegador
            logs = driver.get_log('performance')
            for log in logs:
                if '1234' in log['message']:  # Validar si el código está presente
                    return '1234'
        except WebDriverException:
            # Si ocurre algún error, esperar un segundo antes de reintentar
            time.sleep(1)
    # Si no se encuentra el código, devolver None
    return None
