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

## **README – Projeto de Enriquecimento de Dados com Apache NiFi**

---

### **Descrição do Projeto**
Este projeto tem como objetivo criar um **pipeline de enriquecimento de dados** utilizando o Apache NiFi. Ele conecta uma API externa para coletar informações adicionais (como CEPs), processa e armazena os dados enriquecidos em um banco de dados MySQL. A aplicação dos **Controller Services** no NiFi simplifica e otimiza as conexões, leituras e escritas de dados.

---

## **Pré-requisitos**

1. **Ferramentas necessárias:**
   - Apache NiFi instalado e configurado ([Documentação NiFi](https://nifi.apache.org/))
   - Banco de dados **MySQL** em funcionamento
   - **JDBC Driver** do MySQL instalado
   - API pública ou privada para coleta de dados (por exemplo, API de CEP)
   - Java JDK 8+ para o funcionamento do NiFi

2. **Credenciais e acessos:**
   - Usuário e senha do banco de dados MySQL
   - Acesso à API para coleta de dados

---

## **Passo a Passo do Projeto**

### **1. Configuração do Banco de Dados MySQL**
1. Crie um banco de dados no MySQL:
   ```sql
   CREATE DATABASE dados_enriquecidos;
   ```
2. Crie a tabela para armazenar os dados enriquecidos:
   ```sql
   CREATE TABLE dados_cep (
     id INT AUTO_INCREMENT PRIMARY KEY,
     nome VARCHAR(255),
     cep VARCHAR(20),
     endereco VARCHAR(255),
     bairro VARCHAR(255),
     cidade VARCHAR(255),
     estado VARCHAR(50),
     atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

---

### **2. Instalação e Configuração do Apache NiFi**

1. **Baixe e instale o Apache NiFi**:
   - Link: [Apache NiFi Downloads](https://nifi.apache.org/download.html)

2. **Inicie o Apache NiFi:**
   - No Linux/macOS:
     ```bash
     ./nifi.sh start
     ```
   - No Windows:
     ```bash
     nifi.bat start
     ```

3. Acesse a interface gráfica do NiFi em `http://localhost:8080/nifi`.

---

### **3. Configuração dos Controller Services**

1. **Abra o menu Global**:
   - Na interface NiFi, clique em **Configuration** (ícone no canto superior direito).

2. **Adicione e configure os seguintes Controller Services:**

   #### **DBCPConnectionPool**  
   - **Descrição:** Pool de conexão com o banco MySQL.  
   **Configurações:**
     - **Database Connection URL:** `jdbc:mysql://localhost:3306/dados_enriquecidos`
     - **Database Driver Class Name:** `com.mysql.cj.jdbc.Driver`
     - **Username:** *seu_usuario_mysql*
     - **Password:** *sua_senha_mysql*
     - **Max Total Connections:** 5

   #### **JsonTreeReader**  
   - **Descrição:** Leitor de dados JSON para processamento.

   #### **JsonRecordSetWriter**  
   - **Descrição:** Escritor de dados em formato JSON para armazená-los no banco.

3. **Habilite os Controller Services**:
   - Clique em **Enable** para cada serviço configurado.

---

### **4. Montagem do Fluxo no Apache NiFi**

1. **Arraste os Processors para a tela:**
   - **InvokeHTTP:** Faz a chamada para a API de CEP.
   - **ConvertRecord:** Converte o JSON recebido em um formato processável.
   - **PutDatabaseRecord:** Insere os dados enriquecidos no MySQL.

2. **Configuração dos Processors:**

   #### **InvokeHTTP**
   - **Method:** GET
   - **Remote URL:** *URL da API de CEP*  
   **Exemplo:** `https://viacep.com.br/ws/01001000/json/`
   - **Properties:** Configure para coletar CEPs dinamicamente.

   #### **ConvertRecord**
   - **Record Reader:** `JsonTreeReader`
   - **Record Writer:** `JsonRecordSetWriter`

   #### **PutDatabaseRecord**
   - **Database Connection Pooling Service:** Selecione o `DBCPConnectionPool`.
   - **Table Name:** `dados_cep`

3. **Conecte os Processors:**
   - Conecte o **InvokeHTTP** ao **ConvertRecord** e, em seguida, ao **PutDatabaseRecord**.

4. **Teste o Fluxo:**  
   - Clique em **Start** nos Processors para executar o pipeline.

---

### **5. Teste e Verificação do Pipeline**

1. **Execute uma chamada para a API:**
   - Verifique se a API retorna o JSON esperado com as informações do CEP.

2. **Verifique a inserção no banco de dados:**
   - Após a execução do pipeline, rode a seguinte query no MySQL:
     ```sql
     SELECT * FROM dados_cep;
     ```
   - Verifique se os dados foram inseridos corretamente.

---

### **6. Agendamento e Monitoramento do Pipeline**

1. **Agendamento do Pipeline:**
   - No Processor **InvokeHTTP**, configure o **Scheduling** para rodar automaticamente a cada X minutos.

2. **Monitoramento:**
   - Use a interface do NiFi para monitorar a execução e logs de erros em tempo real.

---

### **7. Solução de Problemas Comuns**

- **Erro de conexão com MySQL:**
  - Verifique se o MySQL está rodando e se a **JDBC URL** está correta.
  - Verifique se o driver MySQL está configurado corretamente no NiFi.

- **Dados não aparecem no MySQL:**
  - Verifique se o nome da tabela no **PutDatabaseRecord** corresponde à tabela criada no banco.

---

### **8. Considerações Finais**

Este pipeline é um exemplo simples de como usar o **Apache NiFi** para enriquecer dados, conectando APIs e bancos de dados em um fluxo contínuo. A modularidade e a facilidade de configuração do NiFi permitem expandir esse projeto para incluir novos endpoints, serviços de validação e relatórios automatizados.

---

### **9. Possíveis Melhorias**

- **Adicionar logs detalhados:** Usar Processors como `LogAttribute` para acompanhar os dados em cada etapa.
- **Incluir mais fontes de dados:** Conectar com outras APIs além da de CEP.
- **Enviar notificações:** Utilizar serviços como **AWS SNS** ou **Twilio** para enviar alertas em caso de erros.
- **Implementar cache:** Evitar chamadas repetidas para a mesma API usando bancos NoSQL como Redis.

---

### **10. Contato**

Se precisar de suporte ou tiver dúvidas sobre este projeto, entre em contato:

- **Autor:** Luciano Vasconcelos  
- **Empresa:** Zapflow  
- **Email:** suporte@suajornadadedados.com.br

---

### **11. Licença**

Este projeto é distribuído sob a licença MIT. Sinta-se à vontade para usar e modificar o código conforme necessário.

---

### **12. Contribuições**

Contribuições são bem-vindas!  
Para contribuir:
1. Fork este repositório.
2. Crie um branch com sua feature: `git checkout -b minha-feature`.
3. Faça o commit das mudanças: `git commit -m "Minha nova feature"`.
4. Abra um pull request.

---

Este README oferece um guia completo para a criação e execução do pipeline de enriquecimento de dados com o Apache NiFi.