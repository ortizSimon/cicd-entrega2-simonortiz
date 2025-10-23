# tests/test_smoke_app.py
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

# Fixture para configurar el navegador (similar a las pruebas de aceptación)
@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecuta sin interfaz gráfica
    options.add_argument("--no-sandbox") # Necesario para algunos entornos
    options.add_argument("--disable-dev-shm-usage") # Necesario para algunos entornos
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_smoke_test(browser):
    """SMOKE TEST: Verifica carga básica y título."""
    # Lee la URL de producción desde una variable de entorno
    app_url = os.environ.get("APP_BASE_URL", "http://localhost:5000")
    print(f"Smoke test ejecutándose contra: {app_url}")
    try:
        browser.get(app_url + "/")
        print(f"Título de la página: {browser.title}")
        assert "To-Do List" in browser.title
        print("Smoke test pasado exitosamente.")
    except Exception as e:
        print(f"Smoke test falló: {e}")
        raise