

# Virtual Store

 Virtual store é um ecommerc feito em django e integrado com o mercado pago. As pessoas do mundo inteira cada vez mais vem usando a internet frequentemente, dessa forma as lojas também não podem ficar para trás,sendo assim resolvi criar uma loja virtual com uma administração simples e de rápido aprendizagem. O sistema atualmente é meramente ficticio, todos os produtos nele são fictícios, assim como o pagamento que é feito com a forma teste do mercado pago, porém não deixando de fugir da realidade e da forma de pagamento real. Este é o [link](https://arcane-woodland-94411.herokuapp.com/) é para ver o site, as informações abaixo tem algumas imagens sobre o site e também como roda-lo na sua propria maquina.


# Layout
   Home           |  Cadastra-se
:-------------------------:|:-------------------------:
![Home](https://github.com/Hernandes-Silva/VOTG/blob/main/imgsGit/gif-Virtual_S.gif)  |  ![register](https://github.com/Hernandes-Silva/Saod-1/blob/main/imgsGit/register.png)

Horários disponiveis            |  Horarios do usuário
:-------------------------:|:-------------------------:


## Pré-requisitos

 Para executar esse projeto é necessario ter instalado na sua maquina o [Python 3](https://www.python.org/downloads/)
 e o [git](https://git-scm.com/)

### Executando o sistema

```bash

# clone o projeto
$ git clone https://github.com/Hernandes-Silva/virtual_store
$ cd virtual_store

#acesse a pasta do projeto com o terminal/cmd e dê o comando:
$  pip install -r requirements.txt

#agora você recisa gerar a secret key do seu projeto e a chaves do mercado pago,
#para isso crie um arquivo .env na raiz do projeto, e coloque nele

MERCADO_PAGO_PUBLIC_KEY=
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
- Os MasterMember:
   - [x] Acessar a administração
   - [X] Ver todas os ultimos pedidos de compra
   - [x] Editar os card da pagina home
- Os Members:
   - [x] Editar os card da pagina home
   - [x] Agendar um horário
   - [x] Desmarca seu hórario agendado
   - [x] Editar suas informações e senha
- Os Usuarios comum podem:
   - [x] cadastra-se
   - [x] colocar itens no carrinho
   - [x] Comprar produtos


## Construido com
* [GitHub](https://github.com/) - O repositório usado
* [Python3](https://www.python.org/downloads/)
* [Django](https://www.djangoproject.com/start/) - O framework web usado



## Author

* [**Hernandes Matheus**](https://github.com/Hernandes-Silva)



## License

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE.md](https://opensource.org/licenses/MIT) para detalhes.
