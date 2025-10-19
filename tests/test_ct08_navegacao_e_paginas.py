# Autor: Raul da Silva Ramos
# CT-ID: CT08 e CT10
import pytest
from selenium.webdriver.common.by import By
from credentials import URL, PROBLEM_USER, PWD, CHECKOUT_FIRST_NAME, CHECKOUT_LAST_NAME, CHECKOUT_POSTAL_CODE

class TestProblemUserNavegacaoPaginas:
    def test_ct08_links_produtos_redirecionam_errado(self, driver):
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.ID, "item_4_title_link").click()

        assert "inventory-item.html?id=5" in driver.current_url, "Não foi redirecionado para a URL incorreta esperada (id=5)."

        nome_produto = driver.find_element(By.CLASS_NAME, "inventory_details_name")
        preco_produto = driver.find_element(By.CLASS_NAME, "inventory_details_price")
        
        assert "Sauce Labs Fleece Jacket" in nome_produto.text, "O nome do produto na página de detalhes está incorreto."
        assert "49.99" in preco_produto.text, "O preço do produto na página de detalhes está incorreto."
        
        imagem_produto = driver.find_element(By.CLASS_NAME, "inventory_details_img")
        assert "sauce-pullover" in imagem_produto.get_attribute("src"), "A imagem na página de detalhes não é a do pullover, que era o esperado para este bug."

    def test_ct10_navegacao_apos_falha_checkout(self, driver):
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys(CHECKOUT_FIRST_NAME)
        driver.find_element(By.ID, "last-name").send_keys(CHECKOUT_LAST_NAME)
        driver.find_element(By.ID, "postal-code").send_keys(CHECKOUT_POSTAL_CODE)
        driver.find_element(By.ID, "continue").click()
        
        assert driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").is_displayed()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "continue-shopping").click()

        assert driver.current_url == f"{URL}inventory.html", "Não retornou à página de inventário."