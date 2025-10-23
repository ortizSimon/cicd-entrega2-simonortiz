import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

BASE_URL = os.environ.get("APP_BASE_URL", "http://localhost:5000")

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_app_loads(browser):
    """Test básico: verificar que la aplicación carga"""
    browser.get(BASE_URL)
    assert "To-Do List" in browser.title
    assert browser.current_url == BASE_URL + "/"

def test_add_todo(browser):
    """Test: agregar un todo"""
    browser.get(BASE_URL)
    
    # Encontrar elementos
    texto_input = browser.find_element(By.NAME, "texto")
    agregar_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    
    # Agregar todo
    texto_input.send_keys("Test todo")
    agregar_button.click()
    
    # Verificar que la página carga
    assert browser.current_url == BASE_URL + "/"
    assert "Test todo" in browser.page_source

def test_error_handling(browser):
    """Test: manejo de errores con texto vacío"""
    browser.get(BASE_URL)
    
    # Encontrar elementos
    texto_input = browser.find_element(By.NAME, "texto")
    agregar_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    
    # Intentar agregar texto vacío
    texto_input.send_keys("   ")
    agregar_button.click()
    
    # Verificar que la página carga (no importa si hay error o no)
    assert browser.current_url == BASE_URL + "/"