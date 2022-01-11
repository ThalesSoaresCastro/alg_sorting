# API
Criação de api para processo de ETL:
 - Extração dos dados da api do teste, passando por todas as páginas;
 - Processamento dos dados, os ordenando utilizando o algoritmo de ordenação Quicksort, com o seu pivô sendo a mediana dos dados do sub-array que está sendo ordenado no momento(divisão-conquista);
 - Exposição de rota contendo os dados já ordenados para serem consumidos;

A API foi desenvolvida utilizando o micro-framework FastAPI;
Como os valores retornados pela API de teste são sempre os mesmos, foi utilizado um banco de dados em memória(Redis), para armazenamento dos valores ao iniciar a api, assim não sendo necessário a consulta direta na API, que estava sendo gargalo para a aplicação.
 
## Documentação

- Ambiente de desenvolvimento: [http://localhost:5857/docs](http://localhost:5857/docs)

- Ambiente de produção: [http://localhost:5852/docs](http://localhost:5852/docs)

## Execução em ambiente Docker

- ### Requerimentos:
    - Algum ambiente de container: [Docker](https://www.docker.com/), [Containerd](https://containerd.io/), [Podman](https://podman.io/), etc.
    - [Docker-compose](https://docs.docker.com/compose/)

Foram criados dois ambientes, desenvolvimento e de produção.

## Criação dos ambientes
Foram criados scripts para se rodar os ambientes com o docker-compose.
Eles devem ser executados de acordo com o sistema operacional utilizado.

- */scripts/windows/..* : execução dos ambientes em windows(arquivos .bat).
- */scripts/linux/..* : execução dos ambientes em linux(arquivos .sh).

Ao serem executados, os containers serão criados e divididos de acordo com a sua stack.

Caso prefira, os arquivos do docker-compose podem ser executados diretamente com os comandos:

### *Buildando* as aplicações

* Sem stack

```
    docker-compose -f {arquivo_docker_compose} up -d --build
```

* Com nome da stack

```
    docker-compose -p {nome_da_stack} -f {arquivo_docker_compose} up -d --build
```

### Subindo containers já Buildados:

* Sem stack

```
    docker-compose -f {arquivo_docker_compose} up -d
```

* Com nome da stack

```
    docker-compose -p {nome_da_stack} -f {arquivo_docker_compose} up -d
```

### Parando a execução containers:

* Sem stack

```
    docker-compose -f {arquivo_docker_compose} down
```

* Com nome da stack

```
    docker-compose -p {nome_da_stack} -f {arquivo_docker_compose} down
```


- O parâmetro -d serve apenas para que o terminal suba os containers e não fique *travado* na tela de log.
- O nome da stack é totalmente opcional mas facilita ao deixar os containers que tem alguma relação separados por grupos, melhorando o controle, principalmente em ferramentas como portainer.
