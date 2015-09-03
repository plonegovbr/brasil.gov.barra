**************************************
.gov.br: Barra de Identidade
**************************************

.. contents:: Conteúdo
   :depth: 2

Introdução
-----------

Este pacote provê a Barra de Identidade do Governo Federal para uso em
sites Plone do Governo da República Federativa do Brasil.

Para saber mais acesse `Identidade Visual do Governo Federal na
Internet <http://epwg.governoeletronico.gov.br/barra/>`_.

Instalação
------------

Para habilitar a instalação deste produto em um ambiente que utilize o
buildout:

1. Editar o arquivo buildout.cfg (ou outro arquivo de configuração) e
   adicionar o pacote ``brasil.gov.barra`` à lista de eggs da instalação::

        [buildout]
        ...
        eggs =
            brasil.gov.barra

2. Após alterar o arquivo de configuração é necessário executar
   ''bin/buildout'', que atualizará sua instalação.

3. Reinicie o Plone

4. Acesse o painel de controle e instale o produto
**Brasil.gov.br: Barra de identidade visual do governo**.

Captura de tela
------------------

Exemplo de uso deste pacote em um site Plone 4.3 com tema padrão:

.. image:: https://github.com/plonegovbr/brasil.gov.barra/raw/master/screenshot.png


Link para o painel de controle:

.. image:: https://github.com/plonegovbr/brasil.gov.barra/raw/master/screenshot-controle1.png

Opções de configuração da barra:

.. image:: https://github.com/plonegovbr/brasil.gov.barra/raw/master/screenshot-controle2.png

Estado deste pacote
---------------------

O **brasil.gov.barra** tem testes automatizados e, a cada alteração em seu
código os testes são executados pelo serviço Travis.

O estado atual dos testes, cobertura dos testes e downloads pode ser visto na imagem a seguir:

.. image:: http://img.shields.io/pypi/v/brasil.gov.barra.svg
    :target: https://pypi.python.org/pypi/brasil.gov.barra

.. image:: https://img.shields.io/travis/plonegovbr/brasil.gov.barra/master.svg
    :target: http://travis-ci.org/plonegovbr/brasil.gov.barra

.. image:: https://img.shields.io/coveralls/plonegovbr/brasil.gov.barra/master.svg
    :target: https://coveralls.io/r/plonegovbr/brasil.gov.barra
