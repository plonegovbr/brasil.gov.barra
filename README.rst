****************************
.gov.br: Barra de Identidade
****************************

.. contents:: Conteúdo
   :depth: 2

Introdução
-----------

Este pacote provê a Barra de Identidade do Governo Federal para uso em sites Plone do Governo da República Federativa do Brasil.

Para saber mais acesse `Identidade Visual do Governo Federal na Internet <http://epwg.governoeletronico.gov.br/barra/>`_.

Instalação
------------

Para habilitar a instalação deste produto em um ambiente que utilize o buildout:

1. Editar o arquivo buildout.cfg (ou outro arquivo de configuração) e adicionar o pacote ``brasil.gov.barra`` à lista de eggs da instalação:

.. code-block:: cfg

    [buildout]
    ...
    eggs =
        brasil.gov.barra

2. Após alterar o arquivo de configuração é necessário executar ''bin/buildout'', que atualizará sua instalação.

3. Reinicie o Plone

4. Acesse o painel de controle e instale o produto **Brasil.gov.br: Barra de identidade visual do governo**.

Captura de telas
----------------

.. figure:: https://raw.githubusercontent.com/plonegovbr/brasil.gov.barra/master/docs/bar.png
    :align: center
    :height: 480px
    :width: 1024px

    A barra de identidade instalada num Plone site padrão.

.. figure:: https://raw.githubusercontent.com/plonegovbr/brasil.gov.barra/master/docs/bar-opened.png
    :align: center
    :height: 480px
    :width: 1024px

    A barra de identidade aberta.

.. figure:: https://raw.githubusercontent.com/plonegovbr/brasil.gov.barra/master/docs/configlet.png
    :align: center
    :height: 480px
    :width: 1024px

    O configlet da barra de identidade no painel de controle.

Estado deste pacote
---------------------

O **brasil.gov.barra** tem testes automatizados e,
a cada alteração em seu código os testes são executados pelo serviço Travis.

O estado atual dos testes, cobertura dos testes e downloads pode ser visto na imagem a seguir:

.. image:: http://img.shields.io/pypi/v/brasil.gov.barra.svg
    :target: https://pypi.python.org/pypi/brasil.gov.barra

.. image:: https://img.shields.io/travis/plonegovbr/brasil.gov.barra/master.svg
    :target: http://travis-ci.org/plonegovbr/brasil.gov.barra

.. image:: https://img.shields.io/coveralls/plonegovbr/brasil.gov.barra/master.svg
    :target: https://coveralls.io/r/plonegovbr/brasil.gov.barra

Atualização de 1.x a 2.x
------------------------

.. Warning::
    Só atualize para a versão 2.x do complemento depois de atualizar à versão mais recente da branch 1.x.

As atualizações da versão 1.x à 2.x só são suportadas das versões mais recentes de cada branch.
Antes de atualizar confira que você está efetivamente utilizando a última versão da branch 1.x e que não existem upgrade steps pendentes de serem aplicados.

Rodando o buildout de uma tag antiga do pacote
----------------------------------------------

Para atender ao relato de ter vários jobs de integração contínua em pacotes brasil.gov.* (ver https://github.com/plonegovbr/portalpadrao.release/issues/11), no fim da seção extends do buildout.cfg de todos os pacotes brasil.gov.* temos a seguinte linha:

.. code-block:: cfg

    https://raw.githubusercontent.com/plonegovbr/portal.buildout/master/buildout.d/versions.cfg

Hoje, esse arquivo contém sempre as versões pinadas de um release a ser lançado. Por esse motivo, quando é feito o checkout de uma tag mais antiga provavelmente você não conseguirá rodar o buildout. Dessa forma, após fazer o checkout de uma tag antiga, recomendamos que adicione, na última linha do extends, o arquivo de versões do IDG compatível com aquela tag, presente no repositório https://github.com/plonegovbr/portalpadrao.release/.

Exemplo: você clonou o repositório do brasil.gov.portal na sua máquina, e deu checkout na tag 1.0.5. Ao editar o buildout.cfg, ficaria dessa forma, já com a última linha adicionada:

.. code-block:: cfg

    extends =
        https://raw.github.com/collective/buildout.plonetest/master/test-4.3.x.cfg
        https://raw.github.com/collective/buildout.plonetest/master/qa.cfg
        http://downloads.plone.org.br/release/1.0.4/versions.cfg
        https://raw.githubusercontent.com/plonegovbr/portal.buildout/master/buildout.d/versions.cfg
        https://raw.githubusercontent.com/plone/plone.app.robotframework/master/versions.cfg
        https://raw.githubusercontent.com/plonegovbr/portalpadrao.release/master/1.0.5/versions.cfg

Para saber qual arquivo de versões é compatível, no caso do brasil.gov.portal, é simples pois é a mesma versão (no máximo um bug fix, por exemplo, brasil.gov.portal é 1.1.3 e o arquivo de versão é 1.1.3.1). Para os demais pacotes, recomendamos comparar a data da tag do pacote e a data nos changelog entre uma versão e outra para adivinhar a versão compatível.
