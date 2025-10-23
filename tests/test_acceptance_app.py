import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

BASE_URL = os.environ.get("APP_BASE_URL", "http://localhost:5000")

# Configuración del driver (elige uno: Chrome o Firefox)
@pytest.fixture
def browser():
    # Opción 1: Chrome (headless - sin interfaz gráfica)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecuta sin interfaz gráfica
    options.add_argument("--no-sandbox") # Necesario para algunos entornos
    options.add_argument("--disable-dev-shm-usage") # Necesario para algunos entornos
    driver = webdriver.Chrome(options=options)

    # Opción 2: Firefox (headless)
    # options = webdriver.FirefoxOptions()
    # options.add_argument("--headless")
    # driver = webdriver.Firefox(options=options)

    # Opción 3: Chrome (con interfaz gráfica - para depuración local)
    # driver = webdriver.Chrome()

    # Opción 4: Firefox (con interfaz gráfica)
    # driver = webdriver.Firefox()
    yield driver
    driver.quit()


# Función de ayuda para esperar y obtener el mensaje
def get_mensaje(browser):
    try:
        # Espera HASTA QUE el <h2> sea visible (máximo 10 segundos)
        mensaje = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h2"))
        )
        return mensaje.text
    except TimeoutException:
        return "Error: Tiempo de espera agotado esperando el mensaje."

#Funcion auxiliar para encontrar elementos:
def find_elements(browser):
    texto_input = browser.find_element(By.NAME, "texto")
    agregar_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    return texto_input, agregar_button

@pytest.mark.parametrize(
    "texto, resultado_esperado",
    [
        ("Hacer ejercicio", "Todo agregado exitosamente"),
        ("Estudiar Python", "Todo agregado exitosamente"),
        ("   ", "Error: El texto del todo no puede estar vacío"),
    ],
)
def test_todo_list(browser, texto, resultado_esperado):
    browser.get(BASE_URL)

    # Encuentra los elementos de la página.  Esta vez con la funcion auxiliar.
    texto_input, agregar_button = find_elements(browser)

    #Realiza la operacion:
    texto_input.send_keys(texto)
    agregar_button.click()

    #Verifica con la funcion auxiliar:
    assert resultado_esperado in get_mensaje(browser)