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

    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute os testes:**

    ```bash
    # Para executar todos os testes
    pytest -v

    # Para executar um arquivo específico
    pytest tests/nome_do_arquivo.py -v
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

### Relação de Testes (18 Casos de Teste)

| ID do Teste | Título da Especificação                                          |
| :---------- | :--------------------------------------------------------------- |
| **CT03**    | Login com Sucesso                                                |
| **CT04**    | Verificação de Imagens Incorretas                                |
| **CT05**    | Validação de Filtro de Ordenação Inoperante (Bug)                |
| **CT06**    | Falha no Fluxo de Checkout (Bug)                                 |
| **CT07**    | Adição e Remoção Múltipla de Itens no Carrinho                   |
| **CT08**    | Redirecionamento Incorreto de Links de Produto (Bug)             |
| **CT09**    | Persistência do Carrinho Após Logout (Bug)                       |
| **CT10**    | Navegação Pós-Falha e Resiliência da Aplicação                   |
| **CT11**    | Validação de Campos Vazios no Checkout                           |
| **CT12**    | Bloqueio de Acesso Direto a Páginas Protegidas                   |
| **CT13**    | Verificação de Responsividade para Visualização Mobile           |
| **CT14**    | Validação de Botão "Remove" Inoperante no Inventário (Bug)       |
| **CT15**    | Integridade de Dados do Inventário ao Carrinho (Bug)             |
| **CT16**    | Jornada do Usuário Indeciso com Item Quebrado (Bug)              |
| **CT17**    | Consistência de Estado da UI Pós-Navegação                       |
| **CT18**    | Vazamento de Estado entre Sessões de Usuários (Bug de Segurança) |
| **CT19**    | Bypass de Fluxo de Checkout pela URL (Bug de Robustez)           |
| **CT20**    | Sincronização Profunda de Estado da UI                           |

---

### Especificações dos Casos de Teste

#### CT03: Login com Sucesso

- **Sinopse:** Validar que o `problem_user` consegue se autenticar com sucesso.
- **Resultado Esperado:** O usuário é redirecionado para a página de inventário.

#### CT04: Verificação de Imagens Incorretas

- **Sinopse:** Confirmar o bug visual onde todas as imagens dos produtos são idênticas.
- **Resultado Esperado:** A contagem de URLs de imagem únicas é igual a 1.

#### CT05: Validação de Filtro Inoperante (Bug)

- **Sinopse:** Confirmar que o filtro de ordenação de produtos não tem efeito.
- **Resultado Esperado:** A ordem dos produtos permanece a mesma após aplicar o filtro.

#### CT06: Falha no Fluxo de Checkout (Bug)

- **Sinopse:** Validar que o `problem_user` não consegue avançar no checkout.
- **Resultado Esperado:** A aplicação exibe uma mensagem de erro na página de checkout.

#### CT07: Adição e Remoção Múltipla no Carrinho

- **Sinopse:** Verificar a consistência do carrinho ao manipular múltiplos itens.
- **Resultado Esperado:** O contador e a lista de itens refletem com precisão as ações.

#### CT08: Redirecionamento Incorreto de Links de Produto (Bug)

- **Sinopse:** Documentar que links de produtos levam a páginas de detalhes erradas.
- **Resultado Esperado:** Clicar no link do "Backpack" (ID 4) leva à página do "Fleece Jacket" (ID 5).

#### CT09: Persistência do Carrinho Após Logout (Bug)

- **Sinopse:** Confirmar que a sessão do carrinho não é limpa após o logout.
- **Resultado Esperado:** Após fazer logout e login novamente, o item da sessão anterior ainda está no carrinho.

#### CT10: Navegação Pós-Falha e Resiliência

- **Sinopse:** Validar que o botão "Continue Shopping" funciona corretamente.
- **Resultado Esperado:** O usuário é redirecionado do carrinho para a página de inventário.

#### CT11: Validação de Campos Vazios no Checkout

- **Sinopse:** Verificar a validação de formulário com campos em branco.
- **Resultado Esperado:** Uma mensagem "Error: First Name is required" é exibida.

#### CT12: Bloqueio de Acesso Direto a Páginas Protegidas

- **Sinopse:** Testar a segurança contra acesso direto a URLs por usuários não logados.
- **Resultado Esperado:** O usuário é redirecionado para a página de login com uma mensagem de erro.

#### CT13: Verificação de Responsividade para Visualização Mobile

- **Sinopse:** Verificar se a interface se adapta a telas de celular.
- **Resultado Esperado:** Elementos essenciais permanecem visíveis em resolução mobile.

#### CT14: Validação de Botão "Remove" Inoperante no Inventário (Bug)

- **Sinopse:** Confirmar que o botão "Remove" na página de inventário não funciona.
- **Resultado Esperado:** Após clicar em "Remove", o estado da interface não se altera.

#### CT15: Integridade de Dados do Inventário ao Carrinho (Bug)

- **Sinopse:** Validar a consistência dos dados e descobrir falhas na adição de itens.
- **Resultado Esperado:** Apenas os itens cujos botões "Add to cart" funcionam são exibidos corretamente no carrinho.

#### CT16: Jornada do Usuário Indeciso com Item Quebrado (Bug)

- **Sinopse:** Simular uma jornada de usuário complexa, descobrindo mais botões inoperantes.
- **Resultado Esperado:** O teste confirma que o botão "Add to cart" do "Fleece Jacket" não funciona, mantendo a consistência do carrinho.

#### CT17: Consistência de Estado da UI Pós-Navegação

- **Sinopse:** Validar se a UI "lembra" o estado do carrinho ao navegar entre páginas.
- **Resultado Esperado:** Ao adicionar um item e voltar para a página de inventário, o botão do item ainda mostra "Remove".

#### CT18: Vazamento de Estado entre Sessões de Usuários (Bug de Segurança)

- **Sinopse:** Validar a falha de segurança onde o carrinho de um usuário vaza para a sessão de outro.
- **Resultado Esperado:** O `standard_user` vê o item do `problem_user` em seu carrinho após o login.

#### CT19: Bypass de Fluxo de Checkout pela URL (Bug de Robustez)

- **Sinopse:** Validar a falha de robustez que permite pular etapas do checkout via URL.
- **Resultado Esperado:** A aplicação permite o acesso direto a `checkout-step-two.html` sem passar pelo passo um.

#### CT20: Sincronização Profunda de Estado da UI

- **Sinopse:** Validar se a UI do inventário reflete uma remoção feita na página do carrinho.
- **Resultado Esperado:** Após remover um item no carrinho e voltar, o botão correspondente no inventário volta a ser "Add to cart".
