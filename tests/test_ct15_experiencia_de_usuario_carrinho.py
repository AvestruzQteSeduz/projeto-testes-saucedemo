# Autor: Raul da Silva Ramos
# CT-ID: CT15
import pytest
from selenium.webdriver.common.by import By
from credentials import URL, PROBLEM_USER, PWD

class TestFluxoComplexo:
    def test_ct15_integridade_dados_e_falha_na_adicao_ao_carrinho(self, driver):
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()

        itens_adicionados_com_sucesso = []

        botao_backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        item_element = botao_backpack.find_element(By.XPATH, "./ancestor::div[@class='inventory_item']")
        nome = item_element.find_element(By.CLASS_NAME, "inventory_item_name").text
        preco = float(item_element.find_element(By.CLASS_NAME, "inventory_item_price").text.replace('$', ''))
        itens_adicionados_com_sucesso.append({'nome': nome, 'preco': preco})
        botao_backpack.click()
        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"

        botao_bikelight = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        item_element = botao_bikelight.find_element(By.XPATH, "./ancestor::div[@class='inventory_item']")
        nome = item_element.find_element(By.CLASS_NAME, "inventory_item_name").text
        preco = float(item_element.find_element(By.CLASS_NAME, "inventory_item_price").text.replace('$', ''))
        itens_adicionados_com_sucesso.append({'nome': nome, 'preco': preco})
        botao_bikelight.click()
        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "2"

        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "2", "O terceiro item foi adicionado, o que não era esperado para este bug."

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        itens_exibidos_no_carrinho = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(itens_exibidos_no_carrinho) == len(itens_adicionados_com_sucesso), "O número de itens no carrinho não corresponde aos adicionados com sucesso."

        for item_local in itens_adicionados_com_sucesso:
            encontrado = False
            for item_carrinho_element in itens_exibidos_no_carrinho:
                if item_local['nome'] == item_carrinho_element.find_element(By.CLASS_NAME, "inventory_item_name").text:
                    encontrado = True
                    break
            assert encontrado, f"O item '{item_local['nome']}' não foi encontrado no carrinho."