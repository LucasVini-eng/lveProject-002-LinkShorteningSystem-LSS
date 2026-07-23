##🔗 Link Shortening System (LSS)O Link Shortening System (LSS) é um serviço interativo desenvolvido em Python para encurtamento, validação e análise de segurança prévia de URLs. 

O objetivo principal da solução é oferecer uma camada de proteção ao usuário final, analisando a URL contra padrões comuns de engenharia social e phishing antes de processar o encurtamento.

### 🛠️ Tecnologias, IDEs & Infraestrutura

O projeto foi construído e implantado utilizando padrões modernos do ecossistema Python 
IDEs de Desenvolvimento:
- PyCharm: Utilizado para desenvolvimento backend, análise estática de código, refatoração segura e gerenciamento de ambientes virtuais (venv).
 - Visual Studio Code (VS Code): Utilizado para ajustes rápidos de estilo (CSS), edição de Markdown, gerenciamento do repositório Git e automações leves.
 - Framework Web: Streamlit (gerenciamento de interface reativa e estados de sessão).
 - Provedor de Encurtamento: pyshorteners integrado à API do TinyURL.
 - Deploy & Hospedagem: Streamlit Community Cloud — implantação contínua (CD) conectada ao repositório GitHub para entrega rápida da aplicação em ambiente de produção na nuvem.

### 🏗️ 1. Desenho de Arquitetura & Visão GeralO sistema utiliza o Streamlit como camada de apresentação e controlador de estado de sessão, desacoplando a lógica de validação de segurança e integração com provedores externos de encurtamento. 
 +-----------------------------------------------------------------------+
 |                        Streamlit Frontend (Cloud)                     |
 |  [ Entrada de URL ]  --->  [ Check URL ]  --->  [ Shorten Button ]    |
 +----------------------------------+------------------------------------+
                                    |
                                    v
 +-----------------------------------------------------------------------+
 |                        Core Application Engine                        |
 |                                                                       |
 |   1. Validator Engine          2. Security & Heuristics               |
 |      (RFC / Format Check)  -->    (HTTPS / Keywords / Extensions)     |
 |                                              |                        |
 |                                              v                        |
 |                                3. External API Integration            |
 |                                   (pyshorteners / TinyURL)            |
 +-----------------------------------------------------------------------+
📋 2. Requisitos do SistemaRequisitos Funcionais (FR)FR-01 - Validação Sintática: O sistema deve verificar se a URL inserida possui formato sintático válido (com suporte a schemas HTTP/HTTPS).FR-02 - Inspeção de Segurança: O sistema deve analisar a URL em busca de elementos suspeitos associados a malwares ou engenharia social antes da geração do link.FR-03 - Encurtamento de URL: O sistema deve gerar um link encurtado apenas para URLs aprovadas nas etapas de validação e segurança.FR-04 - Gestão de Estado: O sistema deve invalidar a checagem de segurança anterior caso o usuário modifique a URL no campo de entrada.Requisitos Não-Funcionais (NFR)NFR-01 - Desempenho / Latência: O tempo de checagem local de heurísticas deve ser near-instantâneo ($< 50\text{ ms}$).NFR-02 - Usabilidade: Interface intuitiva com feedback visual claro (Toasts/Alerts) quanto ao status de segurança do link.NFR-03 - Disponibilidade: Hospedagem em nuvem via Streamlit Cloud garantindo alta disponibilidade sem custos fixos de servidor.📡 3. Interfaces & Endpoints (Mapeamento de Fluxo)Como o sistema opera no modelo Server-Side Rendered (SSR) via WebSockets no Streamlit, as interações do usuário acionam eventos no fluxo da aplicação em vez de requisições HTTP REST clássicas.
