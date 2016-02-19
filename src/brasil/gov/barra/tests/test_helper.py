# -*- coding: utf-8 -*-
from brasil.gov.barra.interfaces import IBarraInstalada
from brasil.gov.barra.testing import INTEGRATION_TESTING
from plone import api
from zope.interface import alsoProvides

import unittest as unittest


class HelperViewTest(unittest.TestCase):
    """ Caso de teste da Browser View BarraHelper"""
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        pp = api.portal.get_tool('portal_properties')
        self.sheet = getattr(pp, 'brasil_gov', None)
        # Como nao eh um teste funcional, este objeto
        # REQUEST precisa ser anotado com o browser layer
        alsoProvides(self.portal.REQUEST, IBarraInstalada)

    def test_helper_view_registration(self):
        """ Validamos se BarraHelper esta registrada"""
        view = api.content.get_view(
            name='barra_helper',
            context=self.portal,
            request=self.portal.REQUEST,
        )
        view = view.__of__(self.portal)
        self.failUnless(view)

    def test_helper_view_local(self):
        """Uso do metodo local"""
        # Obtemos a Browser view
        view = api.content.get_view(
            name='barra_helper',
            context=self.portal,
            request=self.portal.REQUEST,
        )
        # Validamos que ela retorne o valor padrao para
        # o metodo remoto(configurado em profiles/default/propertiestool.xml)
        self.assertFalse(view.local())
        # Alteramos o valor para hospedagem para local
        self.sheet.local = True
        # O resultado da consulta a Browser View deve se adequar
        self.assertTrue(view.local())
