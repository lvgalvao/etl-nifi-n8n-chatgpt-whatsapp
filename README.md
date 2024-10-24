# Workshop ETL Usando Python, AI, N8N e API WhatsApp

## Descrição do Workshop
Uma capacitação completa de 9 horas, ao vivo, onde você aprenderá a criar uma **pipeline avançada** para extração, transformação e integração de dados. Você terá a oportunidade de trabalhar com **Python, N8N, Inteligência Artificial e a API do WhatsApp** para desenvolver soluções reais e escaláveis.

## Parte da Jornada de Dados
Este workshop faz parte da **Jornada de Dados**. Para mais informações, acesse [Jornada de Dados](https://github.com/lvgalvao/data-engineering-roadmap).

## Estrutura do Workshop
### Horário do Workshop
Das 9h às 18h no dia 26/10

### Sobre o Evento
O foco será a **engenharia de dados aplicada à integração de múltiplas fontes**, demonstrando como automatizar processos e lidar com grandes volumes de dados. Durante o workshop, você vai:
- **Processar um arquivo de 1 bilhão de linhas**
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

### Agenda do Workshop
- **Introdução**: O que são ETLs e por que são essenciais em projetos de dados  
- **Extração com Python**: APIs públicas e privadas  
- **Integrações com Airbyte e Apache NiFi**  
- **Automação com N8N e WhatsApp API**  
- **Case Prático**: Processando um arquivo de 1 bilhão de linhas  
- **Trading Automatizado**: Decisões baseadas em dados em tempo real  
- **Monitoramento e Escalabilidade**: Como gerenciar pipelines em produção

## Oferta de Lançamento
**DE: R$497,00**  
**POR: 12x de R$29,69** ou **R$297,00 à vista**  

## Garantia de Satisfação
Se você não estiver satisfeito com o conteúdo do workshop, garantimos a devolução total do valor investido.

## Contato
Ficou com alguma dúvida?  
Envie uma mensagem e converse com uma pessoa real.

---

2024 – Luciano Treinamentos e Consultoria em Dados – Todos os Direitos Reservados

Essa versão atualizada do `README.md` incorpora os detalhes técnicos do projeto de ETL e reflete a estrutura dos arquivos. Com essa nova organização, fica claro para os participantes como o código será utilizado no contexto do workshop, alinhando a prática com a teoria e destacando as ferramentas e automações.