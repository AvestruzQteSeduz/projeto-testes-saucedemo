import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    """
    Fixture que inicializa e configura o WebDriver do Chrome
    antes de cada teste e o fecha ao final.
    """
    chrome_options = webdriver.ChromeOptions()
    
    # --- SOLUÇÃO DEFINITIVA ---
    
    # 1. FORÇA O MODO ANÔNIMO (INCOGNITO)
    # Este é o passo mais eficaz. O modo anônimo inicia uma sessão limpa,
    # sem histórico, cookies ou gerenciamento de senhas salvo, prevenindo os pop-ups.
    chrome_options.add_argument("--incognito")

    # 2. Mantemos os argumentos anteriores como uma camada extra de segurança,
    # embora o modo anônimo já deva resolver o problema.
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-features=PasswordLeakDetection")
    
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    # --- FIM DA ATUALIZAÇÃO ---

    service = ChromeService(ChromeDriverManager().install())
    
    # Passa as opções atualizadas ao criar o WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    yield driver
    
    driver.quit()