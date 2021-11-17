<h1  align="center">Python BackEnd Wallet Cashback🚀</h1>

## 📝 Sobre o projeto

- Esse projeto trata-se de um serviço de tratamento e validações de dados para cadastro de cashback em outro sistema.

- Sobre min:
    Gosto muito de desenvolver em python, espero sempre aprender e contribuir com tudo aquilo que estou participando sempre buscando melhorar minha habilidades.
    
## 🛠️ Tecnologias Utilizadas

[Python](https://www.python.org/)

[FastApi](https://fastapi.tiangolo.com/)

[SqlAlchemy](https://www.sqlalchemy.org/)


## 🔍 Pré-requisitos

[Python](https://www.python.org/)

[Docker](https://www.docker.com/)

[docker-compose](https://docs.docker.com/compose/)



## ⚙️ Como executar o projeto

Para executar o projeto é necessário que instale os pŕe-requesitos acima como docker, docker-compose caso queira utilixar o docker para rodar a aplicação, caso queria rodar ela com python direto na sua maquina, basta o python instlado e bem configurado no seu ambiente.

## .ENV

- Para o rodar o projeto localmente , vai precisar do arquivo .env dentro da pasta /app/ então crie-o colocando o conteudo abaixo.

```text
DEBUG=False
API_URL_REQUEST=https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback
URL=ec2-54-146-82-179.compute-1.amazonaws.com
DATABASE=d1h7osijpd7f9s
USER_DATABASE=rqemedpipcvgxr
PORT_DATABASE=5432
PASSWORD_DATABASE=f26a5298447b74a53d38ae15bf5d4d789a3d5d8fbaf2ad9116945b5b48be7423
URI_DATABASE=postgres://rqemedpipcvgxr:f26a5298447b74a53d38ae15bf5d4d789a3d5d8fbaf2ad9116945b5b48be7423@ec2-54-146-82-179.compute-1.amazonaws.com:5432/d1h7osijpd7f9s
```

Caso queria trocar a aplicação para modo Debug , basta trocar de False para True



### Rodar com Docker
caso queira rodar a aplicação utilizando docker, basta digitar os comando abaixo utilizando o docker-compose.

```bash
# startando o container docker do docker

#comando para buildar a imagen docker
$ docker-compose build

#comando para subir os containers
$ docker-compose up -d

```

### Rodar com Python nativo

 - Se estiver rodando em ambiente Unix basta executar o script run_api.sh que ele criará um maquina virutal python e vai instalar todas dependências nela e executar a aplicação.

 ```bash
    bash run_api.sh
 ```

- Se estiver rodando em ambiente Windows siga os passos abaixo:
  - 1 - Criar um Virtual Env Python com o comando `python -m venv "nome da venv"`
  - 2 - Em seguida temos que ativar essas venv com o comando `cd /"nome da venv"/Scripts/activate`
  - 3 - Com a venv ativada vamos instalar os pacotes com o comando `pip install -r requirements-dev.txt`
  - 4 - Agora já podemos rodar o programa com o comando `python server.py`.



#### Se você seguiu todos os dados Certinho o servidor já está ativo com a aplicação na rota http://127.0.0.1:8000/

### Obs: No ambiente de produção ainda não está configurado a persistência