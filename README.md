# 🔗 Link Shortening System (LSS)

O **Link Shortening System (LSS)** é um serviço interativo desenvolvido em Python para encurtamento, validação e análise de segurança prévia de URLs. O objetivo principal da solução é oferecer uma camada de proteção ao usuário final, analisando a URL contra padrões comuns de **engenharia social e phishing** antes de processar o encurtamento.

---

## 🛠️ Tecnologias, IDEs & Infraestrutura

O projeto foi construído e implantado utilizando padrões modernos do ecossistema Python:

* **IDEs de Desenvolvimento:**
  * **PyCharm:** Utilizado para desenvolvimento backend, análise estática de código, refatoração segura e gerenciamento de ambientes virtuais (`venv`).
  * **Visual Studio Code (VS Code):** Utilizado para ajustes rápidos de estilo (CSS), edição de Markdown, gerenciamento do repositório Git e automações leves.
* **Framework Web:** **Streamlit** (gerenciamento de interface reativa e estados de sessão).
* **Provedor de Encurtamento:** `pyshorteners` integrado à API do **TinyURL**.
* **Deploy & Hospedagem:** **Streamlit Community Cloud** — implantação contínua (CD) conectada ao repositório GitHub para entrega rápida da aplicação em ambiente de produção na nuvem.

---

## 🏗️ 1. Desenho de Arquitetura & Visão Geral

O sistema utiliza o **Streamlit** como camada de apresentação e controlador de estado de sessão, desacoplando a lógica de validação de segurança e integração com provedores externos de encurtamento.

+----------------------------------+------------------------------------+
|                       Streamlit Frontend (Cloud)                      |
|  [ Entrada de URL ]  --->  [ Check URL ]  --->  [ Shorten Button ]    |
+----------------------------------+------------------------------------+
                                   |




