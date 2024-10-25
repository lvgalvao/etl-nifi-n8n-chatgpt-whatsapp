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

## **Quick Start: Como rodar o Apache NiFi**

### **Dockerfile Simplificado**
```dockerfile
# Usando a imagem oficial do Apache NiFi
FROM apache/nifi:latest

# Expondo a porta HTTPS
EXPOSE 8443

# Comando para iniciar o NiFi
CMD ["bin/nifi.sh", "run"]
```

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

  # **Passo a Passo: Conectar uma API e Salvar Dados no PostgreSQL com Apache NiFi**

---

  ```mermaid
  graph TD
    A[InvokeHTTP - Consultar API] --> B[SplitJson - Dividir JSON em itens individuais]
    B --> C[ConvertRecord - Converter JSON para formato tabular]
    C --> D[PutDatabaseRecord - Inserir no PostgreSQL]
    
    subgraph NiFi Controller
        E[DBCPConnectionPool - Conexão com PostgreSQL]
    end

    D --> E
  ```

Este guia irá mostrar como você pode conectar-se a uma **API RESTful** usando o **Apache NiFi** e salvar os dados obtidos em um banco de dados **PostgreSQL**. 

---

## **Pré-requisitos**
1. **Instância do Apache NiFi** rodando em [https://localhost:8443/nifi](https://localhost:8443/nifi)  
2. **Banco de Dados PostgreSQL** ativo com as credenciais e a tabela configuradas.
3. **JDBC Driver do PostgreSQL** disponível para o NiFi.

---

## **Passo 1: Preparar o PostgreSQL**

1. **Crie a Tabela no PostgreSQL**:
   Abaixo está um exemplo de criação de uma tabela chamada `api_data`:
   ```sql
   CREATE TABLE api_data (
       id SERIAL PRIMARY KEY,
       name TEXT,
       age INTEGER,
       email TEXT,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

2. **Instale o Driver JDBC do PostgreSQL**:
   - Baixe o driver PostgreSQL JDBC [aqui](https://jdbc.postgresql.org/download.html).
   - Adicione o arquivo `.jar` ao diretório `lib` do NiFi:
     ```bash
     cp postgresql-<version>.jar /opt/nifi/nifi-current/lib/
     ```

---

## **Passo 2: Criar o Fluxo no NiFi**


1. **Acesse a interface NiFi** em [https://localhost:8443/nifi](https://localhost:8443/nifi).

2. **Adicione e Configure os Componentes**:

### **1. Processador: InvokeHTTP**  
- **Descrição:** Este processador faz a requisição à API.
- **Configuração:**
  - **HTTP Method:** GET
  - **Remote URL:** A URL da API que deseja consultar (ex: https://api.example.com/users)
  - **Attributes to Send:** `All Attributes`
  - **SSL Context Service:** Deixe em branco se a API não exigir HTTPS seguro.
  - **Response Body:** **flowfile-content**

- **Dica:** Teste a API em alguma ferramenta como Postman para garantir que a URL está correta.

---

### **2. Processador: SplitJson**  
- **Descrição:** Divide os dados JSON retornados pela API em itens individuais.
- **Configuração:**
  - **JSONPath Expression:** `$.*`
  - **Destination:** flowfile-content

---

### **3. Processador: ConvertRecord** (Opcional)  
- **Descrição:** Converte o JSON para um formato tabular (como CSV ou Avro).
- **Configuração:**
  - **Record Reader:** Use o **JsonTreeReader**.
  - **Record Writer:** Use um **CSVRecordSetWriter** (ou outro formato suportado).

---

### **4. Processador: PutDatabaseRecord**  
- **Descrição:** Insere os dados no PostgreSQL.
- **Configuração:**
  - **JDBC Connection Pool:** Configure o acesso ao PostgreSQL.
  - **Record Reader:** Use o mesmo leitor que configurou no `ConvertRecord`.
  - **Table Name:** `api_data`
  - **Update Key:** Se necessário, configure uma coluna para updates (ex.: `id`).

---

## **Passo 3: Configurar o Conector JDBC no NiFi**

1. **Adicione um Controller Service**:
   - Clique no botão de configuração no canto superior direito da interface do NiFi.
   - Em **Controller Services**, adicione um novo **DBCPConnectionPool**.

2. **Configure o DBCPConnectionPool**:
   - **Database Connection URL:** `jdbc:postgresql://<host>:<port>/<database>`  
     Exemplo: `jdbc:postgresql://localhost:5432/mydatabase`
   - **Database Driver Class Name:** `org.postgresql.Driver`
   - **Username:** `seu_usuario`
   - **Password:** `sua_senha`

3. **Ative o Controller Service** clicando no botão de ativação.

---

## **Passo 4: Conectar os Processadores e Executar o Fluxo**

1. **Conecte os Processadores** na seguinte ordem:
   - **InvokeHTTP** → **SplitJson** → **PutDatabaseRecord**

2. **Inicie o Fluxo**:
   - Clique no botão de play em cada processador ou no fluxo completo para iniciar.

---

## **Passo 5: Verificar a Inserção no PostgreSQL**

1. Conecte-se ao PostgreSQL e execute uma consulta SQL para verificar os dados inseridos:
   ```sql
   SELECT * FROM api_data;
   ```

---

## **Dicas Adicionais**

- **Logs e Erros:** Verifique os logs do NiFi para encontrar possíveis erros na execução do fluxo.
- **Transformações:** Use o processador **UpdateRecord** se precisar transformar dados antes de inseri-los no banco.
- **Agendamento:** Configure o **InvokeHTTP** para rodar em intervalos regulares e buscar dados periodicamente.

---

## **Comando Docker Útil para Monitoramento**

Se precisar verificar os logs do NiFi:
```bash
docker logs nifi | grep ERROR
```

---

Com este fluxo configurado, você estará pronto para consultar uma API e salvar os dados no PostgreSQL de forma automatizada com o Apache NiFi.