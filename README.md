# Workshop ETL Usando Python, AI, N8N e API WhatsApp

## Descrição do Workshop
Uma capacitação completa de 9 horas, ao vivo, onde você aprenderá a criar uma **pipeline avançada** para extração, transformação e integração de dados. Você terá a oportunidade de trabalhar com **Python, N8N, Inteligência Artificial e a API do WhatsApp** para desenvolver soluções reais e escaláveis.

## Parte da Jornada de Dados
Este workshop faz parte da **Jornada de Dados**. Para mais informações, acesse [Jornada de Dados](https://github.com/lvgalvao/data-engineering-roadmap).

## Estrutura do Workshop
### Horário do Workshop
Das 9h às 18h no dia 26/10

### Agenda do Workshop
- **9h**: Boas-vindas e visão de mercado, desafios de extrair e integrar sistemas
- **10h**: Overview do que vamos construir à tarde
- **10h30**: Planejamento da ETL e crescimento em Python
- **11h30 até 13h**: Apache NiFi
- **13h até 14h**: Almoço
- **14h**: Setup (via SSH) (1HR)
  - Setup VM Ubuntu 22 + Docker
  - Instalação do N8N + Volume Persistente
  - Instalação de SSL
  - Teste de Workflow
  - Boas práticas de escalabilidade
- **15h**: Apresentando o N8N (as Boas) (1HR)
  - Gestão de usuários
  - Gestão de Credenciais
  - Explorando 1000+ conectores
  - Conhecendo o poderoso sistema de Logs
- **16h**: Desafio (2HR)
  - “Criar um robô que coleta o preço do Bitcoin e alerta no WhatsApp/Telegram se houve um recorde de máxima ou mínima da semana”
  - Criar Workflow
  - Preparar API (Realizar teste Postman/Python)
  - Obter informações do preço do Bitcoin 
  - Obter informações da max/min registradas no banco (só relevar 7 dias)
  - Comparar preço atual com records e decidir se alerta ou não
  - Configurar bot Telegram e WhatsApp 
  - Teste final
  - Commit GIT

### Sobre o Evento
O foco será a **engenharia de dados aplicada à integração de múltiplas fontes**, demonstrando como automatizar processos e lidar com grandes volumes de dados. Durante o workshop, você vai:
- Integrar dados de **APIs, SQL e NoSQL**
- Construir pipelines de automação com **Python, N8N e ChatGPT**
- Realizar automações via **WhatsApp**, explorando casos de uso para trading financeiro e análise de mercado.

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
