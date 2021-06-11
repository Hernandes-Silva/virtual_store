

# Virtual Store

 Virtual store é um ecommerc feito em django e integrado com o mercado pago. As pessoas do mundo inteira cada vez mais vem usando a internet frequentemente, dessa forma as lojas também não podem ficar para trás,sendo assim resolvi criar uma loja virtual com uma administração simples e de rápido aprendizagem. O sistema atualmente é meramente ficticio, todos os produtos nele são fictícios, assim como o pagamento que é feito com a forma teste do mercado pago, porém não deixando de fugir da realidade e da forma de pagamento real. Este é o [link](https://arcane-woodland-94411.herokuapp.com/) é para ver o site, as informações abaixo tem algumas imagens sobre o site e também como roda-lo na sua propria maquina.


# Layout
   Login            |  Cadastra-se
:-------------------------:|:-------------------------:
![login](https://github.com/Hernandes-Silva/Saod-1/blob/main/imgsGit/login.png)  |  ![register](https://github.com/Hernandes-Silva/Saod-1/blob/main/imgsGit/register.png)

Horários disponiveis            |  Horarios do usuário
:-------------------------:|:-------------------------:


## Pré-requisitos

 Para executar esse projeto é necessario ter instalado na sua maquina o [Python 3](https://www.python.org/downloads/)
 e o [git](https://git-scm.com/)

### Executando o sistema

```bash

# clone o projeto
git clone https://github.com/Hernandes-Silva/virtual_store
cd virtual_store

#acesse a pasta do projeto com o terminal/cmd e dê o comando:
$  pip install -r requirements.txt

#agora você recisa gerar a secret key do seu projeto e a chaves do mercado pago,
#para isso crie um arquivo .env na raiz do projeto, e coloque nele

MERCADO_PAGO_PUBLIC_KEY=TEST-xxxxxxxxxxxxxxxxxxx
MERCADO_PAGO_ACCESS_TOKEN=
SECRET_KEY=
# depois gere um secret key no terminal copie e cole no secret key do seu projeto
$ python -c "import secrets; print(secrets.token_urlsafe())"


#Agora faça as migrações
$ py manage.py migrate

#Por fim teste a instalação dando o comando
$ python manage.py runserver



```

---
## Features
- Os admin podem:
   - [x] Ver os horários
   - [X] Ver informações sobre quem marcou determinado horários
   - [x] Excluir um horário
   - [x] Criar um procedimento
   - [x] Excluir um procedimento
   - [x] Editar um procedimento
   - [x] Criar um novo administrador
   - [x] Editar suas informações e senha
- Os usuários podem:
   - [x] Ver os horários
   - [x] Agendar um horário
   - [x] Desmarca seu hórario agendado
   - [x] Editar suas informações e senha
- os não usuários podem:
   - [x] cadastra-se
   


## Construido com
* [GitHub](https://github.com/) - O repositório usado pela equipe
* [PHP](https://www.php.net/downloads) - Linguagem de programação utilizada
* [Laravel](https://laravel.com/) - O framework web usado
* [MySQL](https://www.mysql.com/) - O banco de dados usado


## Authors

* [**Hernandes Matheus**](https://github.com/Hernandes-Silva) 
* [**Anna Karoline**](https://github.com/Anna-Karoline) 
* [**Mayara**](https://github.com/mayaramdrs) 



## License

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes
