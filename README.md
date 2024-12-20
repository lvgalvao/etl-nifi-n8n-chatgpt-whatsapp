# Workshop ETL Usando Python, AI, N8N e API WhatsApp

[Link Excalidraw](https://link.excalidraw.com/l/8pvW6zbNUnD/7ih9njnfD2k) 

## Descrição do Workshop
Uma capacitação completa de 9 horas, ao vivo, onde você aprenderá a criar uma **pipeline avançada** para extração, transformação e integração de dados. Você terá a oportunidade de trabalhar com **Python, N8N, Inteligência Artificial e a API do WhatsApp** para desenvolver soluções reais e escaláveis.

## Parte da Jornada de Dados
Este workshop faz parte da **Jornada de Dados**. Para mais informações, acesse [Jornada de Dados](https://github.com/lvgalvao/data-engineering-roadmap).

### Agenda do Workshop

- **9h**: **Boas-vindas e Visão de Mercado**
  - Apresentação Jornada de Dados
  - Apresentação do que será desenvolvido na jornada.
  - Introdução aos desafios de extrair e integrar dados de diferentes sistemas.
  - Principais tendências e oportunidades na automação de dados. 

- **10h**: **Overview do Workshop**
  - Apresentação do projeto que será construído na tarde.
  - Alinhamento de expectativas e objetivos práticos.

- **10h30**: **Planejamento da ETL**
  - Como planejar uma ETL?
  - Como avaliar os requisitos de integração e extração?
  - Estruturando a arquitetura do processo ETL a ser desenvolvido.
  - Fazendo nosso primeiro aquecimento em Python.

- **11h30 até 13h**: **Apache NiFi**
  - Overview do NiFi
  - Implementação de fluxos de dados no NiFi.
  - Salvando nosso código e o desafio da sustentação

- **13h até 14h**: **Intervalo para Almoço**

- **14h**: **Setup de Ambiente (1h)**
  - Conectando via SSH e configurando VM Ubuntu 22 + Docker.
  - Instalação do N8N com volume persistente.
  - Configuração de SSL e segurança básica.
  - Teste de workflow e boas práticas para escalabilidade.

- **15h**: **Explorando o N8N (1h)**
  - Gestão eficiente de usuários e credenciais.
  - Exploração dos 1000+ conectores disponíveis.
  - Utilização e monitoramento do sistema de logs.

- **16h**: **Desafio Prático (2h)**
  - **Objetivo:** Criar um robô para monitorar o preço do Bitcoin e enviar alertas no WhatsApp/Telegram.
    - **Etapas:**
      1. Construção do Workflow no N8N.
      2. Preparação da API e testes no Postman/Python.
      3. Obtenção do preço atual do Bitcoin.
      4. Recuperação das máximas e mínimas dos últimos 7 dias no banco de dados.
      5. Comparação do preço atual com os registros históricos.
      6. Configuração e integração do bot no Telegram e WhatsApp.
      7. Realização de testes finais e validação do processo.
      8. Commit no Git para versionamento.

- **17h00**: **Sorteio e dúvidas**

### Sobre o Evento
O foco será a **engenharia de dados aplicada à integração de múltiplas fontes**, demonstrando como automatizar processos e lidar com grandes volumes de dados. Durante o workshop, você vai:
- Integrar dados de **APIs, SQL e NoSQL**
- Construir pipelines de automação com **Python, N8N e ChatGPT**
- Realizar automações via **WhatsApp**, explorando casos de uso para trading financeiro e análise de mercado.

### **Matriz Comparativa: Apache NiFi, Airbyte e N8N**

| **Critério**                | **Apache NiFi**                                       | **Airbyte**                                      | **N8N**                                          |
|-----------------------------|-------------------------------------------------------|-------------------------------------------------|-------------------------------------------------|
| **Facilidade de uso**        | **Contra**: Curva de aprendizado alta devido à complexidade de configuração. | **A favor**: Interface intuitiva, mais fácil de configurar para pipelines simples. | **A favor**: Interface visual com arraste e solta, ideal para iniciantes. |
| **Escalabilidade**           | **A favor**: Altamente escalável, suporta grandes volumes de dados. | **A favor**: Escalável para pipelines de ingestão de dados em lote. | **Contra**: Menos eficiente para grandes volumes de dados e processos complexos. |
| **Integrações**              | **A favor**: Suporta várias integrações nativas, especialmente para sistemas complexos e IoT. | **A favor**: Focado em integração com bancos de dados e APIs populares. | **A favor**: Grande quantidade de integrações prontas com plataformas e serviços SaaS. |
| **Manutenção e Operação**    | **Contra**: Requer equipe especializada para manutenção contínua. | **A favor**: Foco em simplicidade e facilidade de manutenção. | **A favor**: Simples de operar, com manutenção mínima. |
| **Tempo de Desenvolvimento** | **Contra**: Tempo elevado para configurar pipelines complexos. | **A favor**: Desenvolvimento rápido de pipelines com conectores prontos. | **A favor**: Configuração rápida de automações com baixa necessidade de código. |
| **Custo**                   | **Contra**: Pode ser caro devido à necessidade de infraestrutura robusta. | **A favor**: Open-source com planos pagos apenas para funcionalidades avançadas. | **A favor**: Open-source com modelo freemium e baixo custo inicial. |
| **Comunidade e Suporte**     | **A favor**: Comunidade ativa e documentação extensa. | **A favor**: Comunidade crescente com suporte ativo. | **A favor**: Comunidade ativa e documentação clara, além de muitos tutoriais. |
| **Orquestração de Workflows** | **A favor**: Ideal para workflows complexos e de longa duração. | **Contra**: Menos flexível para orquestrar workflows complexos. | **A favor**: Excelente para automações e workflows simples e médios. |
| **Uso em Tempo Real**        | **A favor**: Otimizado para processamento de dados em tempo real e fluxo contínuo. | **Contra**: Melhor para ingestão em lote do que em tempo real. | **Contra**: Suporta tempo real, mas não é otimizado para grandes fluxos contínuos. |

---

### **Resumo**:
- **Apache NiFi**: Ideal para projetos complexos e de grande escala, mas exige maior expertise técnica. Indicado para casos que envolvem **fluxos de dados contínuos** e **integração com sistemas diversos**.  
- **Airbyte**: Focado em **ingestão de dados estruturados** e **fácil integração com bancos e APIs**, sendo uma solução simples e eficiente para casos de **pipelines em lote**.  
- **N8N**: Perfeito para **automação de processos** e **integrações rápidas**. Embora não seja ideal para grandes volumes de dados, destaca-se pela facilidade de uso e **rápido desenvolvimento** de fluxos.

Essa matriz pode ajudar na escolha da ferramenta com base nas necessidades específicas do projeto, considerando o equilíbrio entre **facilidade de uso, escalabilidade e custo**.

## Tecnologias Utilizadas
- **Python**: Extração e manipulação de dados  
- **N8N**: Automação e orquestração de workflows  
- **SQL & NoSQL**: Armazenamento e integração de dados  
- **API WhatsApp**: Automação de comunicação  
- **Airbyte** e **Apache NiFi**: Alternativas para integração de dados

## Estrutura dos Arquivos de Código
O projeto desenvolvido no workshop está organizado da seguinte forma:

```
src/
├── extract/
│   ├── models/
│   │   └── bitcoin_price_model.py  # Modelagem SQLModel para preços de Bitcoin
│   ├── get_api_v1.py               # Extração básica de API com requests
│   ├── get_api_v2.py               # Extração usando Pydantic para validação
│   └── get_api_v3.py               # Integração com modelo SQLModel
└── pipeline.py                     # Pipeline principal para processar dados
```

### Arquivos e Funções Principais

- **`bitcoin_price_model.py`**:  
  Define a estrutura de dados do preço do Bitcoin usando `SQLModel`.  
  **Exemplo de Classe:**
  ```python
  class BitcoinPrice(SQLModel, table=True):
      id: int | None = Field(default=None, primary_key=True)
      amount: float
      base: str
      currency: str
  ```

- **`get_api_v1.py`**:  
  Primeira versão da função de extração, utilizando `requests` para obter o preço do Bitcoin da API da Coinbase.

- **`get_api_v2.py`**:  
  Utiliza `Pydantic` para validar e modelar a resposta da API, garantindo a integridade dos dados.

- **`get_api_v3.py`**:  
  Integra o modelo de dados `BitcoinPrice` diretamente à extração, facilitando o armazenamento e manipulação.

- **`pipeline.py`**:  
  Conecta todas as partes e executa a pipeline final.  
  **Exemplo:**
  ```python
  from src.extract.get_api_v3 import get_bitcoin_price

  print(get_bitcoin_price())
  ```

### Monitoramento e Escalabilidade
Como gerenciar pipelines em produção.
