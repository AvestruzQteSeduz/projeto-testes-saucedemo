import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import URL, PROBLEM_USER, PWD, STANDARD_USER

class TestFluxosAvancados:
    """
    Escopo: Testes avançados focados em segurança de sessão, fluxos
    adversariais e sincronização profunda do estado da UI.
    """

    def test_ct18_vazamento_de_estado_entre_sessoes_ocorre(self, driver):
        """
        CT18: Valida a falha de segurança onde o estado do carrinho vaza
        entre sessões de usuários diferentes.
        """
        # --- ETAPA 1: SESSÃO DO PROBLEM_USER ---
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        # Adiciona uma espera para garantir que o menu está visível antes de clicar em logout
        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
        
        # --- ETAPA 2: SESSÃO DO STANDARD_USER ---
        driver.find_element(By.ID, "user-name").send_keys(STANDARD_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()

        # --- VALIDAÇÃO DA FALHA DE SEGURANÇA ---
        # Afirma que o carrinho NÃO está vazio, confirmando o vazamento de estado.
        elementos_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(elementos_badge) == 1, "O carrinho estava vazio, indicando que o bug de vazamento de estado foi corrigido."
        assert elementos_badge[0].text == "1"

    def test_ct19_bypass_de_fluxo_pela_url_e_possivel(self, driver):
        """
        CT19: Valida a falha de robustez onde a aplicação permite pular
        uma etapa do fluxo de checkout manipulando a URL.
        """
        # --- ETAPA 1: PREPARAÇÃO ---
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # --- ETAPA 2: TENTATIVA DE BYPASS ---
        driver.get(f"{URL}checkout-step-two.html")

        # --- VALIDAÇÃO DA FALHA DE ROBUSTEZ ---
        # Afirma que a aplicação permaneceu na página de checkout passo 2, confirmando a falha.
        assert "checkout-step-two.html" in driver.current_url, "A aplicação não permitiu pular a etapa do fluxo, indicando que o bug foi corrigido."

    def test_ct20_sincronizacao_profunda_de_estado_da_ui(self, driver):
        """
        CT20: Valida se a UI da página de inventário reflete corretamente
        uma ação de remoção que foi executada em outra página (carrinho).
        """
        # Este teste já estava passando e continua correto.
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(PROBLEM_USER)
        driver.find_element(By.ID, "password").send_keys(PWD)
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        assert driver.find_element(By.ID, "remove-sauce-labs-backpack").is_displayed()
        
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        
        elementos_carrinho = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(elementos_carrinho) == 0
        
        driver.find_element(By.ID, "continue-shopping").click()
        
        wait = WebDriverWait(driver, 5)
        botao_add_to_cart = wait.until(
            EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        assert botao_add_to_cart.is_displayed()
        
        elementos_remove = driver.find_elements(By.ID, "remove-sauce-labs-backpack")
        assert len(elementos_remove) == 0