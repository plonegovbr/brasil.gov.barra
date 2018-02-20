Changelog
---------

1.2.4 (unreleased)
^^^^^^^^^^^^^^^^^^

- Nothing changed yet.


1.2.3 (2018-02-20)
^^^^^^^^^^^^^^^^^^

- Atualiza código da barra local.
  [hvelarde]

- Adiciona suporte ao Python 3.
  [caduvieira]


1.2.2 (2017-11-17)
^^^^^^^^^^^^^^^^^^

- Corrige testes da barra local.
  [caduvieira]


1.2.1 (2017-10-31)
^^^^^^^^^^^^^^^^^^

- Atualiza JavaScript da barra local (closes `#39`_).
  [idgserpro]


1.2 (2016-11-07)
^^^^^^^^^^^^^^^^^^

- Barra local passa a ser o barra.js mas agora dentro do pacote. Foi feita uma
  estrutura na lógica de testes que avisa se a versão do pacote estiver
  desatualizada com relação à barra externa. (closes `#30`_).
  [idgserpro]

- Barra agora é chamada no fim da tag body; Mostra mensagem html, como no
  padrão estabelecido pelo Ministério do Planejamento, se o javascript não
  puder ser carregado (closes `#12`_).
  [idgserpro]

- Adiciona icone da bandeira do Brasil para o configlet do painel de controle.
  [hvelarde]


1.1.1 (2016-07-06)
^^^^^^^^^^^^^^^^^^

- Remove ``@charset 'UTF-8'`` do CSS local para evitar erros de validação;
  o arquivo CSS sempre vai ser entregado usando a codificação certa dentro do Plone.
  [hvelarde]


1.1 (2016-02-19)
^^^^^^^^^^^^^^^^^^

- Atualização da barra local com a barra remota atual (closes `#25`_).
  [rodfersou]

- Remove dependência no unittest2; o pacote nunca foi testado nem estava listado como compatível com o Pyhton 2.6.
  [hvelarde]


1.0.4 (2015-09-03)
^^^^^^^^^^^^^^^^^^

* Remoção do atributo async pois pode causar erro ao executar o script antes do render da página. Obrigado @dadlo. [caduvieira]

* Remoção do protocolo no script para herdar o protocolo (HTTP ou HTTPS)
  [caduvieira]


1.0.3 (2014-12-05)
^^^^^^^^^^^^^^^^^^

* Adição dos atributos de defer e async para a chamada no javascript da barra
  [caduvieira]


1.0.2 (2014-06-11)
^^^^^^^^^^^^^^^^^^

* Englobamos a barra com um div com id barra-identidade, que engloba também o javascript
  [ericof]


1.0.1 (2014-06-10)
^^^^^^^^^^^^^^^^^^

* Uso do plone.api para rotinas internas
  [ericof]

* Corrige o template para remover o script de dentro do div da barra (closes `#10`_)
  [ericof]


1.0 (2014-03-10)
^^^^^^^^^^^^^^^^^^

* Oculta passos de atualização da tela de criação do site
  [ericof]

* Pequenos ajustes na organização do pacote
  [ericof]

* Atualizado produto da barra para ter a mesma aparência da barra
  remota (closes `#7`_).
  [felipeduardo][rodfersou]


1.0a1 (2013-07-22)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Suporte a barra hospedada no endereço barra.brasil.gov.br
  [ericof]
* Suporte a quatro cores da barra
  [ericof]
* Versão inicial do pacote
  [ericof]


.. _`#7`: https://github.com/plonegovbr/brasil.gov.barra/issues/7
.. _`#10`: https://github.com/plonegovbr/brasil.gov.barra/issues/10
.. _`#12`: https://github.com/plonegovbr/brasil.gov.barra/issues/12
.. _`#25`: https://github.com/plonegovbr/brasil.gov.barra/issues/25
.. _`#30`: https://github.com/plonegovbr/brasil.gov.barra/issues/30
.. _`#39`: https://github.com/plonegovbr/brasil.gov.barra/issues/39
