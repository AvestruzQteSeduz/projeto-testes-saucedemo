import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import (
    URL,
    PROBLEM_USER,
    PWD,
    LOGIN_REQUIRED_ERROR
)

class TestProblemUserExcecoesEUsabilidade:
    def test_ct11_validacao_campos_vazios_checkout(self, driver):
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        driver.find_element(By.ID, "continue").click()

        mensagem_erro = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        assert "Error: First Name is required" in mensagem_erro.text
        assert mensagem_erro.is_displayed()

    def test_ct12_acesso_direto_pagina_protegida(self, driver):
        """
        CT12: Garante que um usuário não logado é bloqueado ao tentar
        acessar páginas internas diretamente.
        """
        # Tenta acessar a página de inventário sem login
        driver.get(f"{URL}inventory.html")

        # --- LÓGICA CORRIGIDA ---
        # Valida que foi redirecionado de volta para a página de login
        assert driver.current_url == URL, "Não foi redirecionado para a página de login."

        # Valida a mensagem de erro de acesso
        mensagem_erro = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        assert LOGIN_REQUIRED_ERROR in mensagem_erro.text
        assert mensagem_erro.is_displayed()
        
    def test_ct13_responsividade_mobile(self, driver):
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()

        driver.set_window_size(375, 812)

        menu_hamburguer = driver.find_element(By.ID, "react-burger-menu-btn")
        carrinho_de_compras = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        titulo_produtos = driver.find_element(By.CLASS_NAME, "title")

        assert menu_hamburguer.is_displayed()
        assert carrinho_de_compras.is_displayed()
        assert titulo_produtos.is_displayed()

    def test_ct14_botao_remover_inventario_falha(self, driver):
        """
        CT14: Valida o bug onde o botão 'Remove' na página de
        inventário não funciona.
        """
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()

        # Passo 1: Adicionar ao carrinho e validar a mudança inicial
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        botao_remover = driver.find_element(By.ID, "remove-sauce-labs-backpack")
        assert botao_remover.text.upper() == "REMOVE"
        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"

        # --- LÓGICA CORRIGIDA ---
        # Passo 2: Clicar no botão quebrado
        botao_remover.click()

        # Passo 3: Validar que NADA mudou
        botao_apos_clique = driver.find_element(By.ID, "remove-sauce-labs-backpack")
        assert botao_apos_clique.is_displayed(), "O botão 'Remove' desapareceu."
        assert botao_apos_clique.text.upper() == "REMOVE", "O texto do botão 'Remove' mudou."
        
        contador_apos_clique = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert contador_apos_clique.text == "1", "O contador do carrinho foi alterado."