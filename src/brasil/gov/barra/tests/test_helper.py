# -*- coding: utf-8 -*-
from brasil.gov.barra.browser.barra import BarraViewlet
from brasil.gov.barra.browser.barra_js import BarraViewlet as BarraViewletJs
from brasil.gov.barra.interfaces import IBarraInstalada
from brasil.gov.barra.testing import INTEGRATION_TESTING
from plone import api
from zope.interface import alsoProvides

import unittest as unittest


BARRA_EXTERNA_HTML = u'<script defer="defer" src="//barra.brasil.gov.br/barra.js" type="text/javascript"></script>'
BARRA_LOCAL_LINK_ACESSO_INFORMACAO = u'<a href="http://brasil.gov.br/barra#acesso-informacao" class="link-barra">Acesso à informação</a>'


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

        self.barra_viewlet = BarraViewlet(
            self.portal,
            self.request,
            None,
            None
        )

        self.barra_viewlet_js = BarraViewletJs(
            self.portal,
            self.request,
            None,
            None
        )

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
        self.barra_viewlet.update()
        self.assertFalse(
            BARRA_LOCAL_LINK_ACESSO_INFORMACAO in self.barra_viewlet.render()
        )

        self.barra_viewlet_js.update()
        self.assertTrue(BARRA_EXTERNA_HTML in self.barra_viewlet_js.render())

    def test_helper_true_mostra_barra_local(self):
        """
        Marcando opção local, deve mostrar barra local e não deve aparecer
        barra externa.
        """
        self.sheet.local = True

        self.barra_viewlet.update()
        self.assertTrue(
            BARRA_LOCAL_LINK_ACESSO_INFORMACAO in self.barra_viewlet.render()
        )

        self.barra_viewlet_js.update()
        self.assertFalse(BARRA_EXTERNA_HTML in self.barra_viewlet_js.render())
