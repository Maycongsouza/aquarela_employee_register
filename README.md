# 📄 **README**

---

## 🚀 **INTRODUÇÃO**

### 📂 **Estrutura do Projeto**

---

### **Descrição dos Diretórios**

#### **`database/`**  
Contém arquivos relacionados ao banco de dados, como a conexão, operações CRUD, inicialização do banco e scripts SQL.

#### **`models/`**  
Define as tabelas do banco de dados utilizando SQLAlchemy. Cada modelo representa uma entidade no banco de dados, como **departamentos**, **colaboradores**, **cargos** e **usuários**.

#### **`routers/`**  
Contém a lógica de rotas da aplicação FastAPI, dividida por recursos da aplicação para manter as responsabilidades separadas.

#### **`schemas/`**  
Define os esquemas de validação de dados com Pydantic. Essenciais para garantir a consistência de dados entre as entradas de API e a lógica de negócios.

#### **`tests/`**  
Contém testes unitários para garantir que as funcionalidades principais da aplicação estão funcionando conforme esperado.

#### **`main.py`**  
Ponto de entrada principal da aplicação, onde o servidor FastAPI é iniciado.

---

### 🛠️ **Tecnologias utilizadas**

No projeto foram utilizadas as seguintes tecnologias:

- **Docker e Docker Compose:** Ferramentas essenciais para criar ambientes isolados e consistentes para execução da aplicação, garantindo que a configuração seja facilmente replicável em outros ambientes.
- **Python 3.12:** A linguagem de programação principal do projeto, seguindo as exigências descritas no desafio.
- **PostgreSQL 15:** Foi utilizado como banco de dados principal da aplicação, seguindo as exigências descritas no desafio.

---

### 📚 **Bibliotecas**

Segue a lista de bibliotecas utilizadas:

| **Biblioteca**        | **Breve descrição**                                                     |
|------------------------|-------------------------------------------------------------------------|
| **fastapi**            | Framework moderno para a criação de APIs de forma rápida e eficiente.   |
| **sqlalchemy**         | Ferramenta ORM que simplifica a manipulação de dados no banco de dados. |
| **psycopg2-binary**    | Driver PostgreSQL para conectar o app ao banco de dados PostgreSQL.     |
| **pydantic**          | Validação de dados e estruturação de dados no FastAPI.                  |
| **pytest**             | Ferramenta para realização de testes unitários e automação de testes.   |
| **uvicorn**            | Servidor ASGI usado para rodar a aplicação FastAPI                      |
| **sqlalchemy-utils**    | Extensõe para a SQLAlchemy.                                             |
| **requests**           | Biblioteca para realizar chamadas HTTP.                                 |
| **faker**              | Gerador de dados falsos para testes e simulações no banco de dados.     |

---

### 💡 **Boas práticas**

Durante todo o desenvolvimento do projeto, foram aplicadas boas práticas para garantir um código limpo, legível e fácil de manter:

- **Clean Code:** Prioridade foi dada para um código claro e autoexplicativo, facilitando futuras manutenções.
- **PEP 8:** Seguindo as diretrizes de estilo de código Python.

#### **Padrão de Idioma no Código**

No desenvolvimento deste projeto, **o inglês foi adotado como padrão para nomes de variáveis, funções, classes e outros elementos do código**.

#### **Exceções**
- **Comentários, labels e docstrings**: Estão escritos em **português**, com o objetivo de facilitar o entendimento.

---

### 🏗️ **Estruturação do banco de dados**

O projeto utiliza uma estrutura de banco de dados relacional no **PostgreSQL**. Abaixo estão os detalhes da estrutura e relacionamentos:

Os principais modelos/tabelas definem as entidades e seus relacionamentos:

1. **Department**: Representa os departamentos da organização. Cada departamento possui um líder associado.
2. **Employee**: Representa os colaboradores da empresa. Um colaborador pode estar associado a um departamento e um cargo.
3. **Job**: Representa os cargos da empresa. Determina se um colaborador pode ser líder.
4. **User**: Representa os usuários da aplicação, podendo estar vinculados a um colaborador ou serem independentes.

---

### 🏢 **Relacionamentos e regras do banco**

O banco foi modelado com os seguintes comportamentos e regras:

1. **Departamento e Líder:** Cada departamento possui um líder. O relacionamento é gerenciado pela chave estrangeira `leader_id`.
2. **Regras de liderança:** Apenas uma pessoa pode ocupar o cargo de liderança em seu respectivo departamento.
3. **Triggers:** Lógica implementada no banco de dados para garantir consistência nos relacionamentos:
   - **`enforce_leadership_rules`:** Garante que somente uma pessoa pode atuar como líder de um departamento.
   - **`sync_is_leader`:** Atualiza o campo `is_leader` no colaborador ao alterar o campo `leader_id` no departamento.

---

### 📊 **Estrutura do Banco de Dados**

A seguir, explicações sobre as tabelas utilizadas:

#### 1. **Tabela `Department`**

- **Descrição:** Contém dados sobre os departamentos da empresa.
- **Chaves/Relacionamentos:** `leader_id` é chave estrangeira para identificar o líder do departamento.

---

#### 2. **Tabela `Employee`**

- **Descrição:** Representa os colaboradores da organização.
- **Relacionamentos e condições:**
  - Cada colaborador está associado a um cargo e a um departamento.
  - O campo `is_leader` indica se o colaborador é o líder de seu respectivo departamento.

---

#### 3. **Tabela `Job`**

- **Descrição:** Contém informações sobre os cargos dos colaboradores.
- **Regra importante:** Somente um colaborador pode ocupar um cargo de liderança.

---

#### 4. **Tabela `User`**

- **Descrição:** Representa os usuários no ambiente da aplicação. A relação com a tabela `Employee` é opcional.

---

**Observação Importante:**  
A definição de liderança foi estruturada de forma a garantir que apenas uma pessoa possa atuar como líder para cada departamento, conforme lógica implementada no banco de dados através de **triggers e funções** PostgreSQL.

---

---

### 📄 **Configuração do Arquivo `.env`**

O arquivo `.env` contém variáveis de ambiente essenciais para configurar o banco de dados PostgreSQL no ambiente Docker. Abaixo estão os parâmetros utilizados:

| **Chave**               | **Valor**               | **Descrição**                                                                |
|-------------------------|-------------------------|--------------------------------------------------------------------------------|
| `POSTGRES_USER`         | `admin`                | Nome de usuário do PostgreSQL para autenticação no banco de dados.            |
| `POSTGRES_PASSWORD`     | `admin`                | Senha para autenticação no banco.                          |
| `POSTGRES_DB`           | `human_resources_db`    | Nome do banco de dados principal que será criado no PostgreSQL ao iniciar.     |
| `POSTGRES_HOST`         | `db`                   | Nome do container do banco de dados no ambiente Docker Compose.               |
| `POSTGRES_PORT`         | `5432`                 | Porta padrão para conexão com o banco de dados PostgreSQL.                    |

O arquivo `.env` é carregado pelo Docker Compose para configurar o ambiente de execução.

---

## 🛠️ **COMO USAR**

### **Instalação do Docker e do Docker Compose na máquina**

Para instalar o **Docker** e o **Docker Compose** em distribuições Linux, siga os passos:

#### **1. Atualize seu sistema:**
```bash
sudo apt update && sudo apt upgrade -y
```

#### **2. Instale o Docker:**
```bash
sudo apt install docker.io -y
```

#### **3. Habilite o serviço Docker e inicie:**
```bash
sudo systemctl enable docker
sudo systemctl start docker
```

#### **4. Instale o Docker Compose:**
```bash
sudo apt install docker-compose -y
```

#### **5. Verifique se foi instalado corretamente:**
```bash
docker --version
docker-compose --version
```
**OBS:** Pode ser necessário o sudo.

---

### **Execução**

#### **1. Configurar o ambiente:**

Depois da instalação do Docker, copie o arquivo .env para alocar as variáveis de ambiente dentro do ambiente Docker com o comando:
```bash
sudo apt update && sudo apt upgrade -y
```

#### **2. Executar o ambiente com Docker Compose:**

Navegue até a pasta do projeto onde está localizado o arquivo docker-compose.yml e execute:
```bash
docker-compose up
```
**OBS:** Pode ser necessário o sudo para executar o docker e docker-compose.

### **Em casos de erros**

**Durante os testes, pode ocorrer do Docker "se perder" e o app ser executado antes que o banco de dados esteja pronto. Se isso acontecer:**
```bash
docker-compose down
```

Em seguida, novamente:
```bash
docker-compose up
```

**Caso haja algum erro na execução do aplicativo pelo Docker, você pode tentar subir apenas o PostgreSQL da seguinte forma:**
```bash
docker-compose up db
```

**Após isso, execute o servidor Uvicorn manualmente:**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 5555 --reload
```

**Em caso de erro com as variáveis ambiente que estão no arquivo `env.`, acesso o `conn.py` e defina manualmente**