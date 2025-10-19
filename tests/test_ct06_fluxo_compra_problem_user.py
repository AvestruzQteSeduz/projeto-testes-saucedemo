# Autor: Raul da Silva Ramos
# CT-ID: CT06
from selenium.webdriver.common.by import By
from credentials import (
    URL,
    PROBLEM_USER,
    PWD,
    CHECKOUT_FIRST_NAME,
    CHECKOUT_LAST_NAME,
    CHECKOUT_POSTAL_CODE,
    CHECKOUT_ERROR_MESSAGE
)

class TestProblemUserFluxoCompra:

    def test_ct06_falha_ao_tentar_finalizar_compra(self, driver):
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

        assert driver.current_url == f"{URL}checkout-step-one.html"
        
        mensagem_erro = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        
        assert mensagem_erro.is_displayed(), "A mensagem de erro do checkout não foi exibida."
        assert CHECKOUT_ERROR_MESSAGE in mensagem_erro.text, "O texto da mensagem de erro não é o esperado."