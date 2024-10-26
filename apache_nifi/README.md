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

### **Passo 3: Acessar a Interface NiFi**  
Acesse o NiFi na URL:  
[https://localhost:8443/nifi](https://localhost:8443/nifi)  

---

## **Projeto 01: Conectar API e Salvar Dados no MySQL**

### **Descrição**
Este pipeline conecta-se a uma API de CEP, processa os dados e os armazena em um banco MySQL. O pipeline pode ser executado periodicamente para enriquecer a base de dados com novos CEPs.

---

### **Pré-requisitos**
1. **Banco MySQL ativo**  
2. **JDBC Driver MySQL** adicionado ao NiFi em `/opt/nifi/nifi-current/lib/`  
3. **API de CEP pública** (como `https://viacep.com.br`)

---

### **Montagem do Fluxo no NiFi**

1. **Abra a interface do NiFi.**
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