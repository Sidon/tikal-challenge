# Tikal Tech Dev Challenge
A small test used to evaluate if the candidate has the basic skills:

+ Ability to interpret the problem;
+ Proficiency in Python and Django;
+ Experience with version control.


## Description
There is a system of process tracking which notifies costumers about changes in the process content. 
Some costumers want to integrate their systems via API. 


## TL;DR
[https://coming-soon/](https://www.sidon.net.br/)

## Work Environment:

| Resource          | Description               | Version    |
| :---------------- | :------------------       | :-------   |
| Computer          | Desktop 8 GB Memory       | I5 G5      |
| Operating System  | xenial ubuntu@maui        | 17.03      |
| Editor/IDE        | Pycharm                   | 2017.1.1   |
| venv              | Conda (Miniconda)         | 4.3.14
| Programming language | Python                 |    3.61    |
| CI                | CircleCI                  | 2017-08    |
| Coverage          | Codecov                   |            |
| Django            | Main framework            | 1.11.2     |
| djangorestframework | Framework for api       | 3.6.3      |

## Original Especifications
The original specifications can see on a PDF document on the doc directory

## Description for this implementation
This project implements the original purpose in a way where the API is browseable.
In the root we can see two links, one for process and other for api logs.

Curl Commands:
***********************************

API Root:
============
::

    $ curl https://tikal-challenge.herokuapp.com/api
    {"persons":"https://tikal-challenge.herokuapp.com//persons/",
    "logging":"https://tikal-challenge.herokuapp.com//logging/"}


Inserir usuários do facebook ao banco de dados:
===============================================
::

    $ curl --user user:senha --data "facebookId=4" https://tikal-challenge.herokuapp.com//persons/
    {"facebookId":4,"name":"Mark Zuckerberg","gender":"Not in facebook","email":"Not in facebook",
     "links":{"self":"https://tikal-challenge.herokuapp.com//persons/4/"}}

    $ curl --user user:senha --data "facebookId=1299" https://tikal-challenge.herokuapp.com//persons/
    {"facebookId":1299,"name":"Alexandra Hays","gender":"Not in facebook","email":"Not in facebook",
     "links":{"self":"https://tikal-challenge.herokuapp.com//persons/1299/"}}

    $ curl --user user:senha --data "facebookId=1399" https://tikal-challenge.herokuapp.com//persons/
    {"facebookId":1399,"name":"Sarah Ellison","gender":"Not in facebook","email":"Not in facebook",
     "links": {"self":"https://tikal-challenge.herokuapp.com//persons/1399/"}}

Listar todos os usuarios:
=========================
::

    $ curl --user user:senha https://tikal-challenge.herokuapp.com//persons/
    [{"facebookId":4,"name":"Mark Zuckerberg","gender":"Not in facebook","email":"Not in facebook",
      "links": {"self":"https://tikal-challenge.herokuapp.com//persons/4/"}},
     {"facebookId":1299,"name":"Alexandra Hays","gender":"Not in facebook","email":"Not in facebook",
      "links":{"self":"https://tikal-challenge.herokuapp.com//persons/1299/"}},
     {"facebookId":1399,"name":"Sarah Ellison","gender":"Not in facebook","email":"Not in facebook",
      "links": {"self":"https://tikal-challenge.herokuapp.com//persons/1399/"}}]

Listar somente os dois primeiros usuários:
==========================================
::

    $ curl --user user:senha https://tikal-challenge.herokuapp.com//persons/?limit=2
    [{"facebookId":4,"name":"Mark Zuckerberg","gender":"Not in facebook","email":"Not in facebook",
      "links":{"self":"https://tikal-challenge.herokuapp.com//persons/4/"}},
     {"facebookId":1299,"name":"Alexandra Hays","gender":"Not in facebook","email":"Not in facebook",
      "links":{"self":"https://tikal-challenge.herokuapp.com//persons/1299/"}}]


Listar os dois últimos usuários:
==========================================
::

    $ curl --user user:senha https://tikal-challenge.herokuapp.com//persons/?last=2
    [{"facebookId":1399,"name":"Sarah Ellison","gender":"Not in facebook","email":"Not in facebook","links":
     {"self":"https://tikal-challenge.herokuapp.com//persons/1399/"}},
     {"facebookId":1299,"name":"Alexandra Hays","gender":"Not in facebook","email":"Not in facebook",
      "links":{"self":"https://tikal-challenge.herokuapp.com//persons/1299/"}}]

Excluir um usuário:
====================
::

    curl --user user:senha -X DELETE https://tikal-challenge.herokuapp.com//persons/1399/

Exibir as informações de um usuário:
====================================
::

    $ curl --user user:senha https://tikal-challenge.herokuapp.com//persons/1399/
    {"detail":"Não encontrado."}

    $ curl --user user:senha https://tikal-challenge.herokuapp.com//persons/4/
    {"facebookId":4,"name":"Mark Zuckerberg","gender":"Not in facebook","email":"Not in facebook",
     "links":{"self":"https://tikal-challenge.herokuapp.com//persons/4/"}}

Exibir os logs de acessos:
==========================
::

    $ curl --user user:senha https://tikal-challenge.herokuapp.com//logging/
    {"user":null,"requested_at":"2017-05-16T18:02:49.236681Z","path":"/persons/","remote_addr":"127.0.0.1","host":"127.0.0.1:8007","method":"GET","query_params":"{}","data":null,"response":"\n\n\n\n<!DOCTYPE html>\n<html>\n  <head>\n    \n\n      \n        <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>\n        <meta name=\"robots\" content=\"NONE,NOARCHIVE\" />\n      \n\n      <title>Person List – Django REST framework</title>\n\n      \n        \n          <link rel=\"stylesheet\" type=\"text/css\" href=\"/static/rest_framework/css/bootstrap.min.css\"/>\n          <link rel=\"stylesheet\" type=\"text/css\" href=\"/static/rest_framework/css/bootstrap-tweaks.css\"/>\n        \n\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/static/rest_framework/css/prettify.css\"/>\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/static/rest_framework/css/default.css\"/>\n      \n\n    \n  </head>\n\n  \n  <body class=\"\">\n\n    <div class=\"wrapper\">\n      \n        <div class=\"navbar navbar-static-top navbar-inverse\">\n          <div class=\"container\">\n            <span>\n              \n                <a class='navbar-brand' rel=\"nofollow\" href='http://www.django-rest-framewor
    ...

Acesso a API via browser:
*************************

.. topic:: Hospedado no Heroku, token válido por 2 meses.

    :Raiz: https://tikal-challenge.herokuapp.com//
    :Usuários: https://tikal-challenge.herokuapp.com//persons/
    :Tracking: https://tikal-challenge.herokuapp.com//logging/


Instalação e execução local
***************************

Para execução local, descompactar o arquivo llabs/config/llabs.conf.zip que contem um arquivo do tipo json (llabs.json) com o token para acesso a API do facebook e parte da configuração do arquivo llabs/settings.py.






## API Documentation. 
The api docummenttion can see [here (coming soon)](https://www.sidon.net.br)