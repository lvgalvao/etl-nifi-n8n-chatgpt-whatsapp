# **Apache NiFi - Docker Setup (Quick Start)**

## **Índice**
1. [O que é o Apache NiFi](#o-que-é-o-apache-nifi)  
2. [História do Apache NiFi](#história-do-apache-nifi)  
3. [Conectores e Integrações](#conectores-e-integrações)  
4. [Vantagens do Apache NiFi](#vantagens-do-apache-nifi)  
5. [Empresas que utilizam o Apache NiFi](#empresas-que-utilizam-o-apache-nifi)  
6. [Quick Start: Como rodar o Apache NiFi](#quick-start-como-rodar-o-apache-nifi)  
7. [Comandos Docker úteis](#comandos-docker-úteis)  

---

## **O que é o Apache NiFi**
Apache NiFi é uma plataforma de automação e integração de fluxo de dados que permite mover e transformar dados entre diversos sistemas de forma segura e eficiente, com uma interface visual intuitiva.

---

## **História do Apache NiFi**
Originalmente criado pela NSA sob o nome Niagarafiles, o NiFi foi liberado como open-source pela Apache Software Foundation em 2014. Desde então, se tornou uma ferramenta essencial para integração de dados em tempo real e automação de processos em grandes volumes de dados.

---

## **Conectores e Integrações**
- **Cloud:** AWS S3, Azure Blob Storage, Google Cloud Storage  
- **Bancos de Dados:** MySQL, PostgreSQL, Oracle  
- **Mensageria:** Apache Kafka, MQTT, JMS  
- **APIs:** RESTful, FTP/SFTP, HDFS

---

## **Vantagens do Apache NiFi**
- **Interface visual:** Criação fácil de fluxos com arrastar e soltar  
- **Rastreamento completo:** Proveniência de dados para auditoria  
- **Escalável:** Funciona standalone ou em clusters  
- **Segurança robusta:** Suporte a SSL/TLS e autenticação por usuário único ou LDAP

---

## **Empresas que utilizam o Apache NiFi**
- **Netflix:** Processamento de logs  
- **ING Bank:** Integração de sistemas financeiros  
- **US Air Force:** Monitoramento operacional  
- **CERN:** Análise de dados científicos  

---

### **Passo a Passo para Rodar a Instância**

#### **1. Baixe a Imagem Oficial**
```bash
docker pull apache/nifi:latest
```

#### **2. Execute o Contêiner**
```bash
docker run --name nifi -p 8443:8443 -d apache/nifi:latest
```
- Acesse a interface web em: **[https://localhost:8443/nifi](https://localhost:8443/nifi)**  
- Por padrão, o NiFi gera um nome de usuário e senha aleatórios.

#### **3. Verificar Credenciais**
Use o comando abaixo para visualizar as credenciais geradas:
```bash
docker logs nifi | grep Generated
```

- Exemplo de saída dos logs:
  ```
  Generated Username [USERNAME]
  Generated Password [PASSWORD]
  ```

#### **4. (Opcional) Defina Credenciais Customizadas**
Você pode definir um nome de usuário e senha específicos com o comando:
```bash
docker run --name nifi -p 8443:8443 -d \
  -e SINGLE_USER_CREDENTIALS_USERNAME=admin \
  -e SINGLE_USER_CREDENTIALS_PASSWORD=your_secure_password \
  apache/nifi:latest
```
> **Nota:** A senha deve ter pelo menos 12 caracteres, caso contrário, o NiFi gerará credenciais aleatórias.

---

## **Comandos Docker úteis**

- **Parar o contêiner:**
  ```bash
  docker stop nifi
  ```

- **Reiniciar o contêiner:**
  ```bash
  docker restart nifi
  ```

- **Ver logs:**
  ```bash
  docker logs nifi
  ```

- **Entrar no contêiner:**
  ```bash
  docker exec -it nifi /bin/bash
  ```

## Hello World

### **Exemplo de Processo com FlowFile no Apache NiFi**

Vamos criar um processo simples utilizando o **GenerateFlowFile** para gerar arquivos de 10KB com conteúdo personalizado, simulando dados da **Jornada de Dados**. Esse exemplo demonstra como configurar o processador e como cada configuração impacta o fluxo.

---

### **GenerateFlowFile**: Visão Geral

O **GenerateFlowFile** é um processador que cria FlowFiles com conteúdo gerado dinamicamente. Ele é útil para testes e simulações em pipelines de dados.

---

### **Configurações Importantes do GenerateFlowFile**

1. **Settings (Configurações Gerais):**
   - Define o **comportamento geral** do processador, como nome, penalidade em caso de falha e estado de ativação.
   - **Run Duration:** Tempo que o processador deve permanecer ativo.
   - **Concurrent Tasks:** Define o número de threads paralelas que o processador pode executar.

2. **Scheduling (Agendamento):**
   - Controla **quando e com que frequência** o processador será executado.
     - **Run Schedule:** Determina o intervalo entre execuções. Exemplo: a cada 5 segundos.
     - **Execution:** Pode ser **Timer Driven** (baseado em tempo) ou **Event Driven** (acionado por eventos).
     - **Scheduling Strategy:** Define se o processador rodará por tempo fixo ou volume de dados.

3. **Properties (Propriedades):**
   - Define **comportamentos específicos** para o processador.
     - **File Size:** Define o tamanho dos arquivos. Exemplo: `10 KB`.
     - **Custom Text:** Conteúdo personalizado a ser incluído no FlowFile. Exemplo: `"Bem-vindo à Jornada de Dados!"`
     - **Batch Size:** Quantidade de arquivos gerados por execução.

4. **Comments (Comentários):**
   - Campo livre para adicionar **notas explicativas** sobre o uso ou propósito do processador.

---

### **Exemplo de Configuração do GenerateFlowFile**

1. **Settings:**
   - **Name:** `Geração de Arquivo - Jornada de Dados`
   - **Penalidade:** `30s` (Tempo de espera após falha)
   - **Concurrent Tasks:** 1

2. **Scheduling:**
   - **Run Schedule:** A cada 10 segundos.
   - **Execution:** Timer Driven (baseado em tempo).

3. **Properties:**
   - **File Size:** `10 KB`
   - **Custom Text:** `"Bem-vindo à Jornada de Dados!"`
   - **Batch Size:** `1` (Um arquivo por execução)

4. **Comments:**
   - **Comentário:**  
     “Este processo gera arquivos de 10KB com uma mensagem personalizada da Jornada de Dados para testes e validação.”

---

### **Fluxo de Exemplo com GenerateFlowFile**

```mermaid
flowchart LR
    Generate[GenerateFlowFile] --> Success[Funnel - Captura de Saída]
    Success --> Store[PutFile - Salvar em Diretório]
```

1. **GenerateFlowFile**: Gera um arquivo de 10KB a cada 10 segundos com o texto "Bem-vindo à Jornada de Dados!".
2. **Funnel (Funil)**: Coleta a saída do processador.
3. **PutFile**: Salva os arquivos gerados em um diretório local.

---

### **Como o Processo Funciona**

1. O **GenerateFlowFile** cria um arquivo com 10KB e o texto especificado.
2. Cada arquivo gerado é enviado ao **Funnel**, que direciona a saída para o próximo passo do fluxo.
3. O **PutFile** grava o arquivo gerado em um diretório no sistema local.

---

### **Conclusão**

Este exemplo simples demonstra como configurar e utilizar o **GenerateFlowFile** para criar arquivos personalizados, mostrando a flexibilidade do Apache NiFi. Através das configurações de **Settings, Scheduling, Properties e Comments**, você pode controlar a geração de arquivos para atender às necessidades de teste e automação da **Jornada de Dados**.

## **Projeto de Enriquecimento de Dados com Apache NiFi**

```mermaid
sequenceDiagram
    participant User as Usuário
    participant NiFi as Apache NiFi
    participant MySQL as Banco MySQL
    participant API as API ViaCEP
    participant MySQLFinal as Banco Final

    User->>NiFi: Inicia o processo de ETL
    NiFi->>MySQL: Executa SQL (SELECT cep FROM ceps_unicos)
    MySQL-->>NiFi: Retorna lista de CEPs
    loop Para cada CEP
        NiFi->>API: Requisita dados do CEP (GET)
        API-->>NiFi: Retorna JSON com dados do CEP
        NiFi->>NiFi: Transforma os dados JSON
        NiFi->>MySQLFinal: Insere dados enriquecidos na tabela ceps_completos
    end
    MySQLFinal-->>NiFi: Confirma inserção
    NiFi-->>User: Notifica conclusão do processo
```

**Passo 1: Clonar o Repositório**  
Clone o repositório do projeto:
```bash
git clone https://github.com/Renatoelho/apache-nifi-enriquecimento-cep.git apache-nifi-enriquecimento-cep
cd apache-nifi-enriquecimento-cep/
```

**Passo 2: Rodar com Docker Compose**
Execute o seguinte comando para iniciar o NiFi e o MySQL:
```bash
docker compose -p project-apache-nifi-enriq-cep -f docker-compose.yaml up -d
```

**Passo 3: Acessar a Interface NiFi**  
Acesse o NiFi na URL:  
[https://localhost:8443/nifi](https://localhost:8443/nifi)  

**Montagem do Fluxo no NiFi**

### 1. **Abra a interface do NiFi.**

### 2. **Vamos criar o Flow: Add Process Group**

#### **Passo 1: Add Process Group**
- Clique com o botão direito na interface do NiFi e selecione **"Add Process Group"**.  
- **Nomeie:** *Enriquecimento de CEPs*.

#### **Por que separar por Process Groups?**

1. **Modularidade:**  
   - Cada processo isolado facilita a manutenção e o entendimento.

2. **Separação de Responsabilidades:**  
   - Dividir em grupos como extração, transformação e carga torna cada etapa clara e organizada.

3. **Facilidade no Versionamento:**  
   - Processos independentes permitem versionamento eficiente no Git.

4. **Escalabilidade:**  
   - Ajuste ou execute partes específicas sem parar o fluxo completo.

5. **Ambientes Separados:**  
   - Grupos podem ser facilmente replicados entre desenvolvimento, homologação e produção.

### 3. **Vamos criar os nossos Controller Services**

Os **Controller Services** no Apache NiFi são componentes reutilizáveis que fornecem funcionalidades comuns para vários processadores em um fluxo. Eles garantem **consistência**, **reutilização** e **facilidade de manutenção**, otimizando tarefas como leitura de dados, conexão com bancos e escrita de registros. A seguir, faremos a configuração de três serviços essenciais.

#### **Passo a Passo: Criando os Controller Services**

1. **Adicionar Controller Services:**
   - Dentro do **Process Group**, clique no ícone de engrenagem (**Configure**).  
   - Acesse a aba **Controller Services** e clique em **+** para adicionar novos serviços.

2. **Configurar os Serviços:**
   - Adicione e configure os seguintes **Controller Services**:

---

#### **Lista de Controller Services e Configurações**

##### 1. **JsonTreeReader**
   - **O que faz:**  
     Lê dados em formato JSON para serem utilizados pelos processadores.
   - **Passo:**  
     Adicione o **JsonTreeReader**, e depois vá em **Properties** para definir a estrutura dos dados conforme necessário.

---

##### 2. **JsonRecordSetWriter**
   - **O que faz:**  
     Escreve dados processados em formato JSON, gerando a saída do fluxo.  
   - **Passo:**  
     Adicione o **JsonRecordSetWriter** e configure o formato de saída em **Properties**.

---

##### **3. DBCPConnectionPool (MySQL - Database)**  
- **Descrição:** Gerencia a conexão com o banco de dados MySQL, otimizando a comunicação e o desempenho.  

---

**Configuração:**  
- **Database Connection URL:**  
  `jdbc:mysql://mysql:3306/nifi_db`

- **Database Driver Class Name:**  
  `com.mysql.cj.jdbc.Driver`

- **Database Driver Location:**  
  `/opt/nifi/nifi-current/jdbc/mysql-connector-j-8.0.31.jar`

- **Database User:**  
  `root`

- **Password:**  
  `d8Uwj1wos64h`

- **Validation Query:**  
  `SELECT 1;`  

---

**Passo:**  
1. Adicione o serviço **DBCPConnectionPool** na aba de Controller Services.  
2. Preencha as **Properties** com os valores acima.  
3. Clique em **Enable** para ativar e garantir a conexão correta com o banco.  

---

#### **Habilitar os Controller Services**

1. Após configurar todos os serviços, clique em **Enable** para ativá-los.
2. Verifique se todos estão ativos e sem erros na aba **Controller Services**.

### 4. **Iniciar a Implementação**

Agora que os **Controller Services** estão configurados, vamos configurar um processador para executar nossa query SQL e capturar os dados necessários para o enriquecimento.

---

#### **Passo a Passo: Configuração do Processador ExecuteSQLRecord**

1. **Adicionar o Processador ExecuteSQLRecord:**
   - Na interface do NiFi, clique com o botão direito e selecione **Add Processor**.
   - Escolha **ExecuteSQLRecord** e arraste-o para o fluxo.

2. **Configuração do ExecuteSQLRecord:**
   - Vá em **Properties** e configure os seguintes parâmetros:
     
     - **Database Connection Pooling Service:**  
       `MySQL - Database` (selecionar o serviço de conexão configurado)

     - **SQL select query:**  
       ```sql
       SELECT cep FROM nifi_db.ceps_unicos;
       ```

     - **Record Writer:**  
       `JsonRecordSetWriter` (selecionar o serviço de escrita em JSON configurado)

3. **Criar Funil para Saídas:**
   - Adicione um **Funil (Funnel)** para capturar todas as possíveis saídas do fluxo.
   - Isso garante que qualquer erro, sucesso ou dado processado seja mapeado corretamente.

4. **Objetivo do Processador:**
   - O processador irá consultar o banco de dados e retornar a lista de **CEPs** que precisam ser enriquecidos.
   - Os dados retornados serão processados e enviados como JSON utilizando o **JsonRecordSetWriter**.

### **Alterar o Fluxo para Cada Saída Ser Uma Linha - Ajustando o Max Rows Per Flow File**

1. **Configurar o ExecuteSQLRecord:**
   - Selecione o **ExecuteSQLRecord** e clique em **Configure**.
   - Vá para a aba **Properties**.

2. **Ajuste a Propriedade "Max Rows Per Flow File":**  
   - Defina o valor de **Max Rows Per Flow File** como `1`.

     Isso garantirá que cada registro retornado pela query seja colocado em um **FlowFile** separado.

3. **Verificar a Conexão com o Funil de Sucesso:**  
   - Garanta que o processador **ExecuteSQLRecord** esteja conectado ao **funil de sucesso** para capturar cada linha como um FlowFile independente.

4. **Testar a Alteração:**  
   - Execute o processador e **verifique no funil de sucesso** se cada FlowFile contém exatamente um registro.

### 5. **Mapeamento do JSON**

Nesta etapa, utilizaremos o processador **EvaluateJsonPath** para extrair informações específicas do JSON e mapeá-las como atributos do FlowFile. Isso permitirá que os dados sejam manipulados de forma mais granular no próximo estágio do fluxo.

---

#### **Passo a Passo: Configuração do EvaluateJsonPath**

1. **Adicionar o Processador EvaluateJsonPath:**
   - Na interface do NiFi, clique com o botão direito e selecione **Add Processor**.
   - Escolha **EvaluateJsonPath** e arraste-o para o fluxo.

2. **Conectar à Saída de Sucesso:**  
   - Conecte a **saída de sucesso** do processador **ExecuteSQLRecord** ao **EvaluateJsonPath**.  
   - Isso garante que apenas os registros válidos sejam processados.

3. **Configuração do EvaluateJsonPath:**
   - Vá em **Properties** e adicione a seguinte propriedade:

     - **Property Name:** `cod_cep`  
     - **JsonPath Expression:** `$. [0].cep`  
     - **Destination:** `FlowFile-attribute`  
     - **Return Type:** `json`

---

#### **Adicionar Funil de Saída (Match):**

1. **Criar Funil:**  
   - Adicione um novo **Funil (Funnel)** para capturar as saídas que correspondem ao mapeamento correto (match).

2. **Conectar o EvaluateJsonPath:**  
   - Conecte a **saída de match** do **EvaluateJsonPath** ao **funil**.

---

#### **Testar a Configuração:**

1. **Executar o Fluxo:**  
   - Execute o processador **EvaluateJsonPath** e verifique se o atributo **cod_cep** foi adicionado corretamente aos FlowFiles.

2. **Verificar a Saída:**  
   - Cada FlowFile agora terá o valor do CEP mapeado como um atributo, facilitando o uso posterior em outros processadores ou etapas do fluxo.

### 6. **Configurando Nossa API**

Nesta etapa, vamos configurar um processador **InvokeHTTP** para chamar a API do **ViaCEP**, utilizando o código do CEP mapeado no passo anterior. A resposta será usada para completar os dados na nossa nova tabela no MySQL.

---

#### **Passo a Passo: Configuração do Processador InvokeHTTP**

1. **Adicionar o Processador InvokeHTTP:**
   - Na interface do NiFi, clique com o botão direito e selecione **Add Processor**.
   - Escolha **InvokeHTTP** e arraste-o para o fluxo.

2. **Configuração do InvokeHTTP:**
   - Vá em **Properties** e configure os seguintes parâmetros:

     - **HTTP Method:** `GET`
     - **HTTP URL:**  
       ``` 
       https://viacep.com.br/ws/${cod_cep}/json/ 
       ```  
     - Isso garantirá que cada CEP capturado será enviado como parâmetro na URL da API.

3. **Conectar Saídas:**
   - **Success:** Conecte a saída de sucesso do **InvokeHTTP** ao próximo processador que irá tratar a resposta JSON.
   - **Failure:** Adicione um **funil** para capturar **todos os erros** e conecte a saída **failure** do **InvokeHTTP** a ele.
   - **No Response:** Conecte essa relação também ao **funil de erro** para gerenciar cenários em que a API não responde.

4. **Relacionamento da Saída "Original":**
   - Conecte a saída **original** do **InvokeHTTP** a um funil separado. 
   - Isso garante que a entrada original seja preservada para auditoria ou reprocessamento, caso necessário.

---

#### **Verificar a Tabela Destino**

Vamos consultar a nova tabela no MySQL para garantir que os dados estejam completos após a execução do fluxo.

```sql
SELECT * 
FROM nifi_db.ceps_completos;
```

### 7. **Gravando com PutDatabaseRecord**

Agora vamos adicionar o processador **PutDatabaseRecord** para inserir os dados enriquecidos na tabela **`ceps_completos`** no MySQL.

---

#### **Passo a Passo: Configuração do Processador PutDatabaseRecord**

1. **Adicionar o Processador PutDatabaseRecord:**
   - Na interface do NiFi, clique com o botão direito e selecione **Add Processor**.
   - Escolha **PutDatabaseRecord** e arraste-o para o fluxo.

2. **Configurar as Properties:**
   - **Record Reader:**  
     Selecione `JsonTreeReader` (configurado anteriormente).
   - **Database Connection Pooling Service:**  
     Selecione `MySQL - Database`.
   - **Table Name:**  
     `ceps_completos`
   - **Insert Statement:**  
     O processo será usado para **inserir** os dados enriquecidos na tabela.
   
3. **Conectar Saídas:**
   - **Success:** Conecte ao funil ou ao próximo passo do fluxo.
   - **Failure:** Conecte ao funil de erros para capturar falhas durante a inserção.

4. **Testar Conexão:**  
   - Vá até as **Properties** e clique em **Test Connection** para garantir que o processador está corretamente configurado e pode se conectar ao banco de dados.

---

### 8. **Testando Todo o Fluxo**

1. **Limpar Todas as Filas:**  
   - Antes de ativar, vá até cada funil e fila do fluxo e limpe os dados acumulados para evitar sobrecarga ou resultados antigos.

2. **Ativar Todo o Fluxo:**  
   - Selecione todos os processadores e clique em **Start** para ativá-los simultaneamente.

---

### **Sobre o Schedule do Primeiro Ponto**

1. **Agendamento do Processador Inicial:**
   - No NiFi, o **ExecuteSQLRecord** ou o primeiro processador precisa ter um **schedule** adequado para não sobrecarregar o fluxo.
   - **Recomendações:**
     - Defina o **Run Schedule** para que o processador execute a cada X minutos ou horas, conforme o volume de dados.
     - Use um **Timer Driven Scheduling** caso queira rodar periodicamente, ou **Event-Driven** se o fluxo depender de eventos específicos.
   
2. **Monitoramento:**  
   - Com um agendamento bem definido, você pode evitar gargalos e garantir que as novas inserções sejam processadas de forma eficiente e sem sobrecarga no banco de dados.