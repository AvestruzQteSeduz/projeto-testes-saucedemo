# Autor: Raul da Silva Ramos
# CT-ID: CT03 e CT04
from selenium.webdriver.common.by import By
from credentials import (
    URL,
    PROBLEM_USER,
    PWD
)

class TestProblemUserLoginImagens:

    def test_ct03_login_sucesso(self, driver):
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    def test_ct04_verificar_imagens_quebradas(self, driver):
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()

        imagens_produtos = driver.find_elements(By.CLASS_NAME, "inventory_item_img")
        assert len(imagens_produtos) > 0, "Nenhuma imagem de produto foi encontrada."

        urls_imagens = [img.get_attribute("src") for img in imagens_produtos if img.get_attribute("src")]
        urls_unicas = set(urls_imagens)
        
        assert len(urls_unicas) == 1, "As imagens dos produtos não são todas iguais, o que era esperado para o 'problem_user'."