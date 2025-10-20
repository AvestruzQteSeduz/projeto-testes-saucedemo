# Autor: Raul da Silva Ramos
# CT-ID: CT17
import pytest
from selenium.webdriver.common.by import By
from credentials import URL, PROBLEM_USER, PWD

class TestConsistenciaDeEstado:
    def test_ct17_consistencia_estado_botao_apos_navegacao(self, driver):
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        botao_backpack_remover = driver.find_element(By.ID, "remove-sauce-labs-backpack")
        assert botao_backpack_remover.is_displayed()
        assert botao_backpack_remover.text.upper() == "REMOVE"
        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        assert "cart.html" in driver.current_url
        assert driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack"

        driver.find_element(By.ID, "continue-shopping").click()
        assert "inventory.html" in driver.current_url

        botao_backpack_apos_retorno = driver.find_element(By.ID, "remove-sauce-labs-backpack")
        assert botao_backpack_apos_retorno.is_displayed(), "O botão 'Remove' não está visível após retornar à página de inventário."
        assert botao_backpack_apos_retorno.text.upper() == "REMOVE", "O estado do botão não foi mantido após retornar à página de inventário."