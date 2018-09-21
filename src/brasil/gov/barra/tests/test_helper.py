# -*- coding: utf-8 -*-
from brasil.gov.barra.browser.barra import BarraViewletJs
from brasil.gov.barra.config import BARRA_JS_STATIC_FILE_LOCATION
from brasil.gov.barra.testing import INTEGRATION_TESTING
from plone import api

import os
import unittest


BARRA_JS_URL = 'https://barra.brasil.gov.br/barra_2.0.js'
BARRA_JS_FILE = 'barra.js'
BARRA_JS_STATIC_FILE_LOCATION = os.path.join(
    BARRA_JS_STATIC_FILE_LOCATION, BARRA_JS_FILE)
BARRA_JS_DEFAULT_LANGUAGE = 'pt-BR'

BARRA_EXTERNA_HTML = u'<script defer src="//barra.brasil.gov.br/barra_2.0.js"></script>'
BARRA_LOCAL_HTML = u'<script defer src="++resource++brasil.gov.barra/barra.js"></script>'


class HelperViewTest(unittest.TestCase):
    """ Caso de teste da Browser View BarraHelper"""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.portal.REQUEST
        pp = api.portal.get_tool('portal_properties')
        self.barra_helper = api.content.get_view(
            name='barra_helper',
            context=self.portal,
            request=self.request,
        )
        self.sheet = getattr(pp, 'brasil_gov', None)

        self.barra_viewlet_js = BarraViewletJs(
            self.portal, self.request, None, None)

        # Setup site language settings
        ltool = self.portal.portal_languages
        defaultLanguage = BARRA_JS_DEFAULT_LANGUAGE
        supportedLanguages = [BARRA_JS_DEFAULT_LANGUAGE, 'en', 'es', 'fr']
        ltool.manage_setLanguageSettings(defaultLanguage, supportedLanguages,
                                         setUseCombinedLanguageCodes=False)
        self.ltool = ltool
        self.ltool.setLanguageBindings()

    def test_helper_view_registration(self):
        """ Validamos se BarraHelper esta registrada"""
        view = self.barra_helper.__of__(self.portal)
        self.assertTrue(view)

    def test_helper_view_local(self):
        """Uso do metodo local"""
        # Validamos que ela retorne o valor padrao para
        # o metodo remoto(configurado em profiles/default/propertiestool.xml)
        self.assertFalse(self.barra_helper.local())
        # Alteramos o valor para hospedagem para local
        self.sheet.local = True
        # O resultado da consulta a Browser View deve se adequar
        self.assertTrue(self.barra_helper.local())

    def test_helper_false_mostra_barra_remota(self):
        """
        Não marcando a opção 'local', deve mostrar barra externa e não deve
        aparecer barra interna.
        """
        self.barra_viewlet_js.update()
        self.assertNotIn(BARRA_LOCAL_HTML, self.barra_viewlet_js.render())
        self.assertIn(BARRA_EXTERNA_HTML, self.barra_viewlet_js.render())

    def test_helper_true_mostra_barra_local(self):
        """
        Marcando opção local, deve mostrar barra local e não deve aparecer
        barra externa.
        """
        self.sheet.local = True
        self.barra_viewlet_js.update()
        self.assertIn(BARRA_LOCAL_HTML, self.barra_viewlet_js.render())
        self.assertNotIn(BARRA_EXTERNA_HTML, self.barra_viewlet_js.render())

    def test_js_external_mesma_versao_static(self):
        """
        Baixa a última versão da barra diretamente do servidor do ministério
        do planejamento para ver se a versão da nossa pasta static é a mesma.

        Se não for, avisa no teste e já indica o que tem de ser feito para
        corrigir.
        """
        from filecmp import cmp
        import requests

        barra_js_tmp_location = '/tmp/{0}'.format(BARRA_JS_FILE)  # nosec
        headers = {
            'Accept-Language': BARRA_JS_DEFAULT_LANGUAGE,
            'Cache-Control': 'no-cache',
        }
        r = requests.get(BARRA_JS_URL, headers=headers)

        with open(barra_js_tmp_location, 'wb') as output:
            output.write(r.text.encode('utf-8'))

        iguais = cmp(barra_js_tmp_location, BARRA_JS_STATIC_FILE_LOCATION)

        msg = 'O código da barra está desatualizado; rode o buildout para atualizar'
        self.assertTrue(iguais, msg)
