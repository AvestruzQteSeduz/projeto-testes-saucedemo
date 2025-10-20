# Autor: Raul da Silva Ramos
# CT-ID: CT16
import pytest
from selenium.webdriver.common.by import By
from credentials import URL, PROBLEM_USER, PWD

class TestJornadaDeUsuarioComplexa:
    def test_ct16_jornada_usuario_indeciso_com_bug(self, driver):
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()

        cesta_virtual = {}

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        cesta_virtual['Sauce Labs Backpack'] = 29.99
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        cesta_virtual['Sauce Labs Bike Light'] = 9.99
        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == str(len(cesta_virtual))

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        xpath_remover_bike_light = "//*[div[@class='inventory_item_name' and text()='Sauce Labs Bike Light']]/ancestor::div[@class='cart_item']//button"
        driver.find_element(By.XPATH, xpath_remover_bike_light).click()
        cesta_virtual.pop('Sauce Labs Bike Light')
        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == str(len(cesta_virtual))

        driver.find_element(By.ID, "continue-shopping").click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == str(len(cesta_virtual)), "O contador do carrinho mudou, o que não era esperado para este bug."

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        itens_finais_no_carrinho = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(itens_finais_no_carrinho) == len(cesta_virtual)

        nomes_na_cesta_virtual = sorted(cesta_virtual.keys())
        nomes_no_carrinho_real = sorted([item.find_element(By.CLASS_NAME, "inventory_item_name").text for item in itens_finais_no_carrinho])

        assert nomes_na_cesta_virtual == nomes_no_carrinho_real, "A lista final de itens no carrinho não corresponde à esperada."