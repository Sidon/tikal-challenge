######################################
``Tikal Tech Dev Challenge``
######################################


.. topic:: Description

    There is a system of process tracking which notifies costumers about changes in the process content.
    Some costumers want to integrate their systems via API.

    A small test used to evaluate if the candidate has the basic skills:

    + Ability to interpret the problem;
    + Proficiency in Python and Django;
    + Experience with version control.

    :Date: **27/02/2018**
    :Author: **Sidon Duarte**


TL;DR
*****
A aplicação foi hospedada no `Heroku <http://www.heroku.com>`_ . Para testá-la, `Clique aqui <https://tikal-challenge.herokuapp.com/>`_ .

Work Environment:
******************

    +-------------------+---------------------------+------------+
    | Resource          | Description               | Version    |
    +===================+===========================+============+
    | Computer          | Desktop 8 GB Memory       | I5 G5      |
    +-------------------+---------------------------+------------+
    | Operating System  | xenial ubuntu@maui        | 17.03      |
    +-------------------+---------------------------+------------+
    | Editor/IDE        | Pycharm                   | 2017.1.1   |
    +-------------------+---------------------------+------------+
    | venv              | Conda (Miniconda)         | 4.3.14     |
    +-------------------+---------------------------+------------+
    | Devel Platform    + Django/Python             |    3.61    |
    +-------------------+---------------------------+------------+
    | CI                | CircleCI                  | 2017-08    |
    +-------------------+---------------------------+------------+
    | Coverage          | Codecov                   |            |
    +-------------------+---------------------------+------------+
    | Django            | Main framework            | 1.11.2     |
    +-------------------+---------------------------+------------+
    | DRF               | dajano-rest-fw            |  3.6       |
    +-------------------+---------------------------+------------+


Original Especifications
***************************

The original specifications can see on a PDF document on the doc directory

## Description for this implementation
This project implements the original purpose in a way where the API is browseable.
In the root we can see two links, one for process and other for api logs.

Comandos Curl
***********************************

API Root:
============
::

    $ curl https://tikal-challenge.herokuapp.com/api/
    {"api/processos":"https://tikal-challenge.herokuapp.com/api/api/processos/",
    "api/logging":"https://tikal-challenge.herokuapp.com/api/api/logging/"}


Listar os processos
=========================
::

    curl -H 'Accept: application/json; indent=4' -u admin:master.21 https://tikal-challenge.herokuapp.com/api/api/processos/
    {
        "count": 13,
        "next": "https://tikal-challenge.herokuapp.com/api/api/processos/?page=2",
        "previous": null,
        "results": [
            {
                "user": 1,
                "numero_processo": "00000000000000000001",
                "dados_processo": "Amet porttitor eget dolor morbi. Magna fringilla urna porttitor rhoncus. In vitae turpis massa sed elementum.",
                "links": {
                    "self": "https://tikal-challenge.herokuapp.com/api/api/processos/32/"
                }
            },



Listar somente os dois primeiros processos:
===============================================
::

    curl --user user:senha https://tikal-challenge.herokuapp.com/api/api/processos/?limit=2
    {"count":2,"next":null,"previous":null,"results":
    [{"user":1,"numero_processo":"00000000000000000001","dados_processo":"Amet porttitor eget dolor morbi. Magna fringilla urna porttitor rhoncus. In vitae turpis massa sed elementum.","links":{"self":"https://tikal-challenge.herokuapp.com/api/api/processos/32/"}},{"user":1,"numero_processo":"00000000000000000002","dados_processo":"Et malesuada fames ac turpis egestas. Cursus risus at ultrices mi tempus imperdiet.","links":{"self":"https://tikal-challenge.herokuapp.com/api/api/processos/33/"}}]}


Listar os dois últimos processos:
==========================================
::

    curl --user user:senha https://tikal-challenge.herokuapp.com/api/api/processos/?last=2
    {"count":2,"next":null,"previous":null,"results":[{"user":1,"numero_processo":"97700225000000000000","dados_processo":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras pellentesque facilisis ullamcorper. Maecenas gravida vel ligula quis gravida.","links":{"self":"https://tikal-challenge.herokuapp.com/api/api/processos/43/"}},{"user":1,"numero_processo":"12345600000000000000","dados_processo":"Et mel laudem percipitur intellegebat. Ne sumo doctus pro, nam postea tritani noluisse no. Vix at sumo habeo convenire, nibh dolor nominavi ei mea.","links":{"self":"https://tikal-challenge.herokuapp.com/api/api/processos/44/"}}]}


Excluir um processo:
====================
::

    curl --user user:senha -X DELETE https://tikal-challenge.herokuapp.com/api/processos/9999/


Exibir os logs de acessos:
==========================
::

   $ curl --user user:senha https://tikal-challenge.herokuapp.com/api/api/logging/

...

Acesso a API via browser:
*************************

.. topic:: Hospedado no Heroku.

    :Raiz: https://tikal-challenge.herokuapp.com/api/
    :Processos: https://tikal-challenge.herokuapp.com/api/api/processos/
    :Tracking: https://tikal-challenge.herokuapp.com/api/api/logging/


Instalação e execução local
***************************
Para execução local, descompactar o arquivo /config/tikal.conf.zip que contem um arquivo do tipo json
(tikal.json) que precisa ser criptografado, como o comando: ./manage.py crypt


Dados Iniciais
****************
Para gerar os dados iniciais execute:

    $ ./manage.py initialdata

Limpar as migrações
**********************
Para limpar as migraçoes execute:

    $ ./manage.py clmigrations


