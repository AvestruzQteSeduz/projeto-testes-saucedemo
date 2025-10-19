# Autor: Raul da Silva Ramos
# CT-ID: CT03 e CT04
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from credentials import (
    URL,
    PROBLEM_USER,
    PWD
)

class TestProblemUserFiltro:

    @pytest.fixture(autouse=True)
    def setup_login(self, driver):
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()

    def test_ct05_filtro_nao_funciona(self, driver):
        """
        CT05: Validar que o filtro de ordenação de produtos não tem efeito
        para o 'problem_user'.
        """

        nomes_produtos_antes = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        ordem_antes = [nome.text for nome in nomes_produtos_antes]

        filtro_select_element = driver.find_element(By.CLASS_NAME, "product_sort_container")
        filtro = Select(filtro_select_element)
        filtro.select_by_value("za")

        nomes_produtos_depois = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        ordem_depois = [nome.text for nome in nomes_produtos_depois]

        assert ordem_antes == ordem_depois, "A ordem dos produtos mudou, o que não era esperado para o 'problem_user'."