# -*- coding: utf-8 -*-

from brasil.gov.barra.browser.barra import BarraViewletJs
from brasil.gov.barra.config import BARRA_JS_DEFAULT_LANGUAGE
from brasil.gov.barra.config import BARRA_JS_FILE
from brasil.gov.barra.config import BARRA_JS_STATIC_FILE_LOCATION
from brasil.gov.barra.config import BARRA_JS_URL
from brasil.gov.barra.interfaces import IBarraInstalada
from brasil.gov.barra.testing import INTEGRATION_TESTING
from filecmp import cmp
from plone import api
from time import time
from zope.component import getMultiAdapter
from zope.interface import alsoProvides

import unittest
import urllib2


BARRA_EXTERNA_HTML = u'<script defer="defer" src="//barra.brasil.gov.br/barra.js" type="text/javascript"></script>'
BARRA_LOCAL_HTML = u'<script defer="defer" src="++resource++brasil.gov.barra/barra.js" type="text/javascript"></script>'


class HelperViewTest(unittest.TestCase):
    """ Caso de teste da Browser View BarraHelper"""
    layer = INTEGRATION_TESTING

    def language_lowercase(self):
        """
        @return: Two-letter string lowercase, the active language code
        """
        context = self.layer['portal']
        portal_state = getMultiAdapter((context, context.REQUEST), name=u'plone_portal_state')
        current_language = portal_state.language()
        return current_language.lower()

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
            self.portal,
            self.request,
            None,
            None
        )

        # Setup site language settings
        ltool = self.portal.portal_languages
        defaultLanguage = BARRA_JS_DEFAULT_LANGUAGE
        supportedLanguages = [BARRA_JS_DEFAULT_LANGUAGE, 'en', 'es', 'fr']
        ltool.manage_setLanguageSettings(defaultLanguage, supportedLanguages,
                                         setUseCombinedLanguageCodes=False)
        self.ltool = ltool
        self.ltool.setLanguageBindings()

        # Como nao eh um teste funcional, este objeto
        # REQUEST precisa ser anotado com o browser layer
        alsoProvides(self.portal.REQUEST, IBarraInstalada)

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
        self.assertFalse(BARRA_LOCAL_HTML in self.barra_viewlet_js.render())
        self.assertTrue(BARRA_EXTERNA_HTML in self.barra_viewlet_js.render())

    def test_helper_true_mostra_barra_local(self):
        """
        Marcando opção local, deve mostrar barra local e não deve aparecer
        barra externa.
        """
        self.sheet.local = True
        self.barra_viewlet_js.update()
        self.assertTrue(BARRA_LOCAL_HTML in self.barra_viewlet_js.render())
        self.assertFalse(BARRA_EXTERNA_HTML in self.barra_viewlet_js.render())

    def test_js_external_mesma_versao_static(self):
        """
        Baixa a última versão da barra diretamente do servidor do ministério
        do planejamento para ver se a versão da nossa pasta static é a mesma.

        Se não for, avisa no teste e já indica o que tem de ser feito para
        corrigir.
        """
        prevent_cache_random_string = str(time()).split('.')[0]
        url = '{0}?v={1}'.format(BARRA_JS_URL + '.' + self.language_lowercase(), prevent_cache_random_string)
        barra_js_tmp_location = '/tmp/{0}'.format(BARRA_JS_FILE)
        request = urllib2.Request(
            url,
            headers={'Accept-Language': BARRA_JS_DEFAULT_LANGUAGE}
        )

        barra_js = urllib2.urlopen(request)

        with open(barra_js_tmp_location, 'wb') as output:
            output.write(barra_js.read())

        iguais = cmp(barra_js_tmp_location, BARRA_JS_STATIC_FILE_LOCATION)

        # Caso esse teste falhe, rode o comando
        # wget --header="Accept-Language: BARRA_JS_DEFAULT_LANGUAGE" http://barra.brasil.gov.br/barra.js?v=$RANDOM && mv barra.js\?v=* barra.js
        # em seu terminal para pegar a última versão da barra para poder fazer
        # o teste passar. BARRA_JS_DEFAULT_LANGUAGE vem do config.py.
        self.assertTrue(iguais)
