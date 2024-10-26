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

# **README – Projeto de Enriquecimento de Dados com Apache NiFi**

---

## **Índice**
1. [O que é o Apache NiFi](#o-que-é-o-apache-nifi)  
2. [História do Apache NiFi](#história-do-apache-nifi)  
3. [Conectores e Integrações](#conectores-e-integrações)  
4. [Vantagens do Apache NiFi](#vantagens-do-apache-nifi)  
5. [Quick Start: Rodando o NiFi com Docker](#quick-start-rodando-o-nifi-com-docker)  
6. [Projeto 01: Conectar API e Salvar Dados no MySQL](#projeto-01-conectar-api-e-salvar-dados-no-mysql)  
7. [Criação Automática de Tabelas no Banco](#criação-automática-de-tabelas-no-banco)  
8. [Solução de Problemas Comuns](#solução-de-problemas-comuns)

---

## **O que é o Apache NiFi**  
Apache NiFi é uma ferramenta de automação de fluxo de dados que permite movimentar, transformar e integrar dados entre sistemas de forma eficiente e segura.

---

## **História do Apache NiFi**  
Desenvolvido pela NSA e liberado pela Apache em 2014, o NiFi se tornou essencial para projetos de integração de dados em tempo real.

---

## **Conectores e Integrações**
- **Cloud:** AWS S3, Azure Blob Storage, Google Cloud Storage  
- **Bancos de Dados:** MySQL, PostgreSQL, Oracle  
- **Mensageria:** Apache Kafka, MQTT  
- **APIs:** RESTful, FTP/SFTP

---

## **Vantagens do Apache NiFi**
- **Interface visual:** Simples e intuitiva  
- **Escalável:** Pode rodar standalone ou em clusters  
- **Rastreamento:** Proveniência completa de dados  
- **Segurança:** SSL/TLS e autenticação LDAP

---

## **Quick Start: Rodando o NiFi com Docker**

### **Passo 1: Clonar o Repositório**  
Clone o repositório do projeto:
```bash
git clone https://github.com/Renatoelho/apache-nifi-enriquecimento-cep.git apache-nifi-enriquecimento-cep
cd apache-nifi-enriquecimento-cep/
```

### **Passo 2: Rodar com Docker Compose**
Execute o seguinte comando para iniciar o NiFi e o MySQL:
```bash
docker compose -p project-apache-nifi-enriq-cep -f docker-compose.yaml up -d
```

#### ** Nosso arquivo docker compose **

## **Comentário sobre os Volumes no `docker-compose`**

Volumes são uma maneira eficiente de armazenar dados de contêineres de forma persistente, garantindo que as informações não sejam perdidas caso o contêiner seja reiniciado ou removido. A seguir, detalhamos os volumes utilizados para o **Apache NiFi** e **MySQL** no seu `docker-compose.yaml`.

---

### **Volumes Criados para o Apache NiFi**

1. **`nifi-logs:/opt/nifi/nifi-current/logs`**  
   - **Descrição:** Armazena todos os logs gerados pela aplicação NiFi.  
   - **Importância:** Permite a auditoria e o monitoramento de erros, além de análises posteriores sobre o desempenho do sistema.

2. **`nifi-conf:/opt/nifi/nifi-current/conf`**  
   - **Descrição:** Contém os arquivos de configuração do NiFi.  
   - **Importância:** Garante que todas as configurações personalizadas sejam preservadas entre reinicializações do contêiner.

3. **`nifi-state:/opt/nifi/nifi-current/state`**  
   - **Descrição:** Armazena informações sobre o estado dos processadores e fluxos do NiFi.  
   - **Importância:** Mantém o estado dos processadores para garantir a continuidade dos fluxos após falhas ou reinícios.

4. **`nifi-content:/opt/nifi/nifi-current/content_repository`**  
   - **Descrição:** Repositório para armazenar temporariamente os dados em trânsito pelos fluxos do NiFi.  
   - **Importância:** Otimiza o desempenho, armazenando conteúdo enquanto os dados são processados e transferidos entre processadores.

5. **`nifi-database:/opt/nifi/nifi-current/database_repository`**  
   - **Descrição:** Repositório que contém informações sobre o repositório de banco de dados do NiFi.  
   - **Importância:** Garante a persistência dos dados internos do NiFi que não devem ser perdidos entre reinicializações.

6. **`nifi-flowfile:/opt/nifi/nifi-current/flowfile_repository`**  
   - **Descrição:** Armazena informações sobre os **FlowFiles** (unidades de dados em trânsito).  
   - **Importância:** Essencial para a recuperação e rastreamento de dados em caso de falhas durante o processamento.

7. **`nifi-provenance:/opt/nifi/nifi-current/provenance_repository`**  
   - **Descrição:** Mantém o histórico de proveniência de todos os dados processados pelo NiFi.  
   - **Importância:** Facilita auditorias e rastreamento de dados, garantindo conformidade e transparência sobre como os dados foram manipulados.

---

### **Volumes Criados para o MySQL**

1. **`mysql-database:/var/lib/mysql:rw`**  
   - **Descrição:** Armazena todos os dados do banco de dados MySQL.  
   - **Importância:** Garante a persistência dos dados do banco, mesmo que o contêiner seja reiniciado ou removido.

2. **`./mysql/deploy/init:/docker-entrypoint-initdb.d`**  
   - **Descrição:** Diretório local contendo scripts de inicialização do banco.  
   - **Importância:** Permite a execução de scripts SQL ao iniciar o contêiner, como a criação de tabelas ou inserções iniciais.

---

### **Por que Utilizar Volumes?**

1. **Persistência de Dados:** Volumes garantem que os dados e configurações do sistema não sejam perdidos entre reinicializações e atualizações de contêineres.
2. **Separação de Dados e Aplicação:** Permite que dados críticos fiquem fora do ciclo de vida dos contêineres, facilitando backups e migrações.
3. **Fácil Manutenção:** Logs e arquivos de configuração podem ser acessados diretamente no sistema host para análise e ajustes.
4. **Compartilhamento entre Contêineres:** Volumes permitem que múltiplos contêineres acessem os mesmos dados, como no caso de bancos de dados.

---

### **Configuração de Rede e Acesso**

O projeto usa uma rede personalizada (`nifi-network`) com **subnet 10.16.0.0/24**. Isso permite que os serviços **NiFi** e **MySQL** se comuniquem diretamente, utilizando os IPs fixos atribuídos a cada contêiner.

---

Com essa estrutura de volumes, seu ambiente Docker está bem organizado para garantir **resiliência, persistência e rastreamento de dados**. Além disso, ao utilizar volumes nomeados e diretórios montados, você facilita o gerenciamento dos dados e a manutenção da aplicação.

### **Passo 3: Acessar a Interface NiFi**  
Acesse o NiFi na URL:  
[https://localhost:8443/nifi](https://localhost:8443/nifi)  

---

version: "3.3"

services: 
  apache-nifi:
    hostname: apache-nifi
    image: apache/nifi:1.23.0
    container_name: apache-nifi
    ports:
      - "8443:8443"
    deploy:
      resources:
        limits:
          cpus: "0.95"
          memory: 4G
    restart: on-failure
    environment:
      - SINGLE_USER_CREDENTIALS_USERNAME=nifi
      - SINGLE_USER_CREDENTIALS_PASSWORD=HGd15bvfv8744ghbdhgdv7895agqERAo
      - TZ=America/Sao_Paulo
    healthcheck:
      test: wget -q --spider http://apache-nifi:8443/nifi-api/system-diagnostics || exit 1
      interval: 60s
      timeout: 40s
      retries: 3
    volumes: 
      - ./nifi/jdbc:/opt/nifi/nifi-current/jdbc
      - nifi-logs:/opt/nifi/nifi-current/logs
      - nifi-conf:/opt/nifi/nifi-current/conf
      - nifi-state:/opt/nifi/nifi-current/state
      - nifi-content:/opt/nifi/nifi-current/content_repository
      - nifi-database:/opt/nifi/nifi-current/database_repository
      - nifi-flowfile:/opt/nifi/nifi-current/flowfile_repository
      - nifi-provenance:/opt/nifi/nifi-current/provenance_repository
    networks:
      nifi-network:
        ipv4_address: 10.16.0.2
  mysql:
    depends_on:
      - apache-nifi
    hostname: mysql
    image: mysql:5.7.40
    container_name: mysql
    command: mysqld --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
    volumes:
      - mysql-database:/var/lib/mysql:rw
      - ./mysql/deploy/init:/docker-entrypoint-initdb.d
    ports:
      - "3306:3306"
    deploy:
      resources:
        limits:
          cpus: "0.95"
          memory: 2G
    restart: always
    environment:
      - MYSQL_ROOT_PASSWORD=d8Uwj1wos64h
      - MYSQL_DATABASE=nifi_db
      - TZ=America/Sao_Paulo
    healthcheck:
      test: mysqladmin ping -h mysql -u root -pd8Uwj1wos64h || exit 1
      interval: 30s
      timeout: 20s
      retries: 5
    networks:
      nifi-network:
        ipv4_address: 10.16.0.3

volumes:
  nifi-logs:
  nifi-conf:
  nifi-state:
  nifi-content:
  nifi-database:
  nifi-flowfile:
  nifi-provenance:
  mysql-database:

networks:
  nifi-network:
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 10.16.0.0/24
---

### **Montagem do Fluxo no NiFi**

1. **Abra a interface do NiFi.**
2. **Vamos criar o Flow**

### 2. **Vamos criar o Flow: Add Process Group**

#### **Passo 1: Add Process Group**
- Clique com o botão direito na interface do NiFi e selecione **"Add Process Group"**.  
- **Nomeie:** *Enriquecimento de CEPs*.

---

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

---

### 3. **Vamos criar os nossos Controller Services**

Os **Controller Services** no Apache NiFi são componentes reutilizáveis que fornecem funcionalidades comuns para vários processadores em um fluxo. Eles garantem **consistência**, **reutilização** e **facilidade de manutenção**, otimizando tarefas como leitura de dados, conexão com bancos e escrita de registros. A seguir, faremos a configuração de três serviços essenciais.

---

#### **Passo a Passo: Criando os Controller Services**

1. **Adicionar Controller Services:**
   - Dentro do **Process Group**, clique no ícone de engrenagem (**Configure**).  
   - Acesse a aba **Controller Services** e clique em **+** para adicionar novos serviços.

2. **Configurar os Serviços:**
   - Adicione e configure os seguintes **Controller Services**:

---

### **Lista de Controller Services e Configurações**

#### 1. **JsonTreeReader**
   - **O que faz:**  
     Lê dados em formato JSON para serem utilizados pelos processadores.
   - **Passo:**  
     Adicione o **JsonTreeReader**, e depois vá em **Properties** para definir a estrutura dos dados conforme necessário.

---

#### 2. **JsonRecordSetWriter**
   - **O que faz:**  
     Escreve dados processados em formato JSON, gerando a saída do fluxo.  
   - **Passo:**  
     Adicione o **JsonRecordSetWriter** e configure o formato de saída em **Properties**.

---

#### **3. DBCPConnectionPool (MySQL - Database)**  
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

---

### **Resumo**

O uso dos **Controller Services** garante que as conexões e leituras sejam consistentes e reutilizáveis, otimizando o fluxo de dados. Cada serviço configurado centraliza uma funcionalidade importante para evitar redundâncias e facilitar a manutenção.


2. **Adicione e configure os processadores:**

#### **Processador: InvokeHTTP**  
- **Descrição:** Faz requisições à API de CEP.
- **Configuração:**  
  - **URL:** `https://viacep.com.br/ws/${cep}/json/`
  - **Method:** GET

#### **Processador: ConvertRecord**  
- **Descrição:** Converte JSON para um formato tabular.
- **Configuração:**  
  - **Record Reader:** JsonTreeReader  
  - **Record Writer:** JsonRecordSetWriter  

#### **Processador: PutDatabaseRecord**  
- **Descrição:** Insere os dados no banco MySQL.
- **Configuração:**  
  - **JDBC Connection Pool:** DBCPConnectionPool  
  - **Table Name:** `ceps_completos`

---

## **Criação Automática de Tabelas no Banco**

### **Rotina de Inicialização**  
Ao iniciar o projeto, as seguintes tabelas serão criadas automaticamente no MySQL:

#### **Tabela: ceps_unicos**  
Armazena CEPs únicos provenientes de diferentes sistemas.
```sql
CREATE TABLE IF NOT EXISTS nifi_db.ceps_unicos (
    id INT NOT NULL AUTO_INCREMENT,
    origem VARCHAR(30),
    cep VARCHAR(10),
    datahora_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

INSERT INTO nifi_db.ceps_unicos (cep, origem)
VALUES
('01153000', 'Sistema A'),
('20050000', 'Sistema B'),
('70714020', 'Sistema C');
```

#### **Tabela: ceps_completos**  
Armazena o resultado completo do enriquecimento dos CEPs.
```sql
CREATE TABLE IF NOT EXISTS nifi_db.ceps_completos (
    id INT AUTO_INCREMENT,
    cep VARCHAR(10),
    logradouro VARCHAR(255),
    complemento VARCHAR(255),
    bairro VARCHAR(255),
    localidade VARCHAR(255),
    uf VARCHAR(2),
    ibge VARCHAR(10),
    gia VARCHAR(255),
    ddd VARCHAR(5),
    siafi VARCHAR(10),
    datahora_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);
```

---

## **Configuração dos Controller Services**

### **1. Configurar o DBCPConnectionPool**  
- **Database URL:** `jdbc:mysql://localhost:3306/nifi_db`  
- **Driver:** `com.mysql.cj.jdbc.Driver`  
- **Username:** *seu_usuario*  
- **Password:** *sua_senha*  

### **2. Configurar Leitores e Escritores de Registros**  
- **JsonTreeReader:** Lê os dados JSON retornados pela API.  
- **JsonRecordSetWriter:** Prepara os dados para inserção no banco MySQL.

---

## **Execução do Pipeline**

1. **Conecte os Processors:**  
   - **InvokeHTTP** → **ConvertRecord** → **PutDatabaseRecord**

2. **Inicie o Fluxo:**  
   Clique no botão de **play** para rodar o pipeline.

3. **Verifique os Dados no MySQL:**  
   Execute a seguinte query para verificar a inserção:
   ```sql
   SELECT * FROM nifi_db.ceps_completos;
   ```

---

## **Solução de Problemas Comuns**

- **Erro de Conexão com MySQL:**  
  Verifique se o banco está rodando e se o driver JDBC está corretamente configurado.

- **Dados Não Aparecem no Banco:**  
  Confirme se a tabela no `PutDatabaseRecord` corresponde ao nome da tabela no banco.

- **Erro na API:**  
  Teste a API manualmente para garantir que ela está disponível.

---

## **Considerações Finais**

Este projeto demonstra como integrar APIs e bancos de dados usando o Apache NiFi. A modularidade do NiFi permite expandir facilmente o pipeline para incluir novos endpoints e serviços de validação.

---

### **Comandos Docker Úteis**

- **Parar o NiFi:**  
  ```bash
  docker stop nifi
  ```

- **Reiniciar o NiFi:**  
  ```bash
  docker restart nifi
  ```

- **Verificar Logs:**  
  ```bash
  docker logs nifi
  ```

---

Com este guia, você tem todas as instruções necessárias para configurar o **NiFi**, conectar-se a uma **API**, enriquecer dados e armazená-los em um **banco MySQL**.