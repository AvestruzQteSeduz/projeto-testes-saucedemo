# tests/test_ct07_carrinho_e_sessao.py

import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from credentials import URL, PROBLEM_USER, PWD

class TestProblemUserCarrinhoSessao:
    """
    Escopo: Testes de interação com o carrinho e estado da sessão
    para o 'problem_user'.
    """

    def test_ct07_adicao_remocao_multipla_carrinho(self, driver):
        """
        CT07: Valida a consistência do carrinho ao adicionar e
        remover múltiplos itens.
        """
        # Passo 1: Login
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()

        # Passo 2: Adiciona o primeiro item e valida o contador
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"

        # Passo 3: Adiciona o segundo item e valida o contador
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "2"

        # Passo 4: Navega para o carrinho e valida os itens
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        itens_no_carrinho = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(itens_no_carrinho) == 2, "O número de itens no carrinho está incorreto."

        # Passo 5: Remove um item e valida o estado
        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        itens_no_carrinho_apos_remocao = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(itens_no_carrinho_apos_remocao) == 1, "Item não foi removido corretamente."
        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1", "Contador do carrinho não atualizou após remoção."

    def test_ct09_carrinho_persiste_apos_logout(self, driver):
        """
        CT09: Valida que o carrinho de compras persiste entre sessões
        (não é limpo) após o logout, caracterizando um bug.
        """
        # Passo 1: Login e adiciona item ao carrinho
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        # Passo 2: Faz o logout
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        driver.find_element(By.ID, "logout_sidebar_link").click()
        assert driver.current_url == URL, "Não redirecionou para a página de login após logout."

        # Passo 3: Faz login novamente
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()

        # --- LÓGICA CORRIGIDA ---
        # Passo 4: Valida que o carrinho NÃO está vazio, confirmando o bug
        elementos_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(elementos_badge) == 1, "O carrinho estava vazio, o que não era o comportamento esperado para este bug."