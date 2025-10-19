# Projeto de Testes Automatizados - Sauce Demo

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)

## Sobre o Projeto

Este repositório contém uma suíte de testes automatizados desenvolvida como projeto final para a disciplina de **Qualidade e Teste de Software (QTS)** do curso de Desenvolvimento de Sistemas.

O objetivo principal foi mapear e documentar o comportamento da plataforma de e-commerce [Sauce Demo](https://www.saucedemo.com), focando especificamente no escopo do usuário **`problem_user`**. A automação foi utilizada como ferramenta de investigação para identificar, validar e caracterizar tanto as funcionalidades operantes quanto os bugs, erros e inconsistências apresentados por este tipo de usuário.

## Tecnologias Utilizadas

- **Linguagem:** Python 3.13
- **Framework de Teste:** Pytest
- **Automação de Navegador:** Selenium WebDriver
- **Gerenciamento de Drivers:** webdriver-manager
- **Gerenciamento de Ambiente:** venv

## Como Executar

Para executar a suíte de testes localmente, siga os passos abaixo.

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    cd SEU_REPOSITORIO
    ```

2.  **Crie e ative o ambiente virtual:**

    ```bash
    # Criar o ambiente
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    (Certifique-se de ter um arquivo `requirements.txt`. Se não tiver, crie-o com `pip freeze > requirements.txt`)

    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute os testes:**
    ```bash
    pytest -v
    ```

---

## Plano de Testes e Cenários Mapeados

| Campo               | Descrição                                                         |
| :------------------ | :---------------------------------------------------------------- |
| **Disciplina**      | Qualidade e Teste de Software (QTS)                               |
| **Sistema Alvo**    | Plataforma de E-commerce Sauce Demo (`https://www.saucedemo.com`) |
| **Escopo do Teste** | Usuário do tipo `problem_user`                                    |
| **Autores**         | Raul da Silva Ramos, Matheus, Rafael, Pedro H, Ryan V.            |

### Propósito

O objetivo deste plano de testes é mapear e documentar sistematicamente o comportamento da aplicação Sauce Demo sob a perspectiva do usuário `problem_user`. A finalidade é identificar, validar e caracterizar tanto as funcionalidades que operam conforme o esperado quanto os bugs, erros e inconsistências apresentados.

### Relação de Testes

| ID do Teste | Título da Especificação                                   |
| :---------- | :-------------------------------------------------------- |
| **CT03**    | Login com Sucesso                                         |
| **CT04**    | Verificação de Imagens Incorretas na Página de Inventário |
| **CT05**    | Validação de Filtro de Ordenação Inoperante               |
| **CT06**    | Falha no Fluxo de Checkout                                |
| **CT07**    | Adição e Remoção Múltipla de Itens no Carrinho            |
| **CT08**    | Redirecionamento Incorreto de Links de Produto            |
| **CT09**    | Persistência do Carrinho Após Logout                      |
| **CT10**    | Navegação Pós-Falha e Resiliência da Aplicação            |

---

### Especificações dos Casos de Teste

#### CT03: Login com Sucesso

- **Sinopse:** Validar que o `problem_user` consegue se autenticar com sucesso.
- **Resultado Esperado:** O usuário é redirecionado para a página de inventário (`/inventory.html`).

#### CT04: Verificação de Imagens Incorretas

- **Sinopse:** Confirmar o bug visual onde todas as imagens dos produtos na página de inventário são idênticas.
- **Resultado Esperado:** A contagem de URLs de imagem únicas é igual a 1.

#### CT05: Validação de Filtro Inoperante

- **Sinopse:** Confirmar o bug funcional onde o filtro de ordenação de produtos não tem efeito.
- **Resultado Esperado:** A ordem dos produtos na página permanece a mesma após a aplicação do filtro.

#### CT06: Falha no Fluxo de Checkout

- **Sinopse:** Validar o bug que impede o `problem_user` de avançar no processo de checkout.
- **Resultado Esperado:** A aplicação permanece na página de checkout e exibe uma mensagem de erro.

#### CT07: Adição e Remoção Múltipla no Carrinho

- **Sinopse:** Verificar a consistência do carrinho de compras ao manipular múltiplos itens.
- **Resultado Esperado:** O contador e a lista de itens no carrinho refletem com precisão todas as ações de adição e remoção.

#### CT08: Redirecionamento Incorreto de Links de Produto

- **Sinopse:** Documentar o bug onde links de produtos levam a páginas de detalhes erradas, que exibem imagens de terceiros produtos.
- **Resultado Esperado:** Ao clicar no link do "Backpack" (ID 4), o usuário é levado à página do "Fleece Jacket" (ID 5).

#### CT09: Persistência do Carrinho Após Logout

- **Sinopse:** Confirmar o bug onde a sessão do carrinho não é encerrada, fazendo com que os itens persistam após o logout e um novo login.
- **Resultado Esperado:** Após fazer logout e login novamente, o item adicionado na sessão anterior ainda está no carrinho.

#### CT10: Navegação Pós-Falha e Resiliência

- **Sinopse:** Validar que o botão "Continue Shopping" na página do carrinho funciona corretamente.
- **Resultado Esperado:** O usuário é redirecionado da página do carrinho de volta para a página de inventário.

#### CT11: Validação de Campos Vazios no Checkout

- **Sinopse:** Verificar a validação de formulário com campos em branco no checkout.
- **Resultado Esperado:** Uma mensagem de erro "Error: First Name is required" é exibida.

#### CT12: Bloqueio de Acesso Direto a Páginas Protegidas

- **Sinopse:** Testar a segurança contra acesso direto a URLs internas por usuários não logados.
- **Resultado Esperado:** O usuário é redirecionado para a página de login e uma mensagem de erro é exibida.

#### CT13: Verificação de Responsividade para Visualização Mobile

- **Sinopse:** Verificar se a interface se adapta a telas de celular.
- **Resultado Esperado:** Elementos essenciais (menu, carrinho, título) permanecem visíveis em uma resolução de 375x812 pixels.

#### CT14: Validação de Botão "Remove" Inoperante (Bug)

- **Sinopse:** Confirmar o bug onde o botão "Remove" na página de inventário não funciona.
- **Resultado Esperado:** Após clicar em "Remove", o estado da interface (botão e contador do carrinho) não se altera.
