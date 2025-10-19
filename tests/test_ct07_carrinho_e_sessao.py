# Autor: Raul da Silva Ramos
# CT-ID: CT07 e CT09
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from credentials import URL, PROBLEM_USER, PWD

class TestProblemUserCarrinhoSessao:
    def test_ct07_adicao_remocao_multipla_carrinho(self, driver):
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"

        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "2"

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        itens_no_carrinho = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(itens_no_carrinho) == 2, "O número de itens no carrinho está incorreto."

        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        itens_no_carrinho_apos_remocao = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(itens_no_carrinho_apos_remocao) == 1, "Item não foi removido corretamente."
        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1", "Contador do carrinho não atualizou após remoção."

    def test_ct09_carrinho_persiste_apos_logout(self, driver):
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        driver.find_element(By.ID, "react-burger-menu-btn").click()
        driver.find_element(By.ID, "logout_sidebar_link").click()
        assert driver.current_url == URL, "Não redirecionou para a página de login após logout."

        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()

        elementos_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(elementos_badge) == 1, "O carrinho estava vazio, o que não era o comportamento esperado para este bug."