# -*- coding: utf-8 -*-
from brasil.gov.barra.interfaces import IBarraInstalada
from brasil.gov.barra.testing import INTEGRATION_TESTING
from zope.interface import alsoProvides

import unittest2 as unittest


class HelperViewTest(unittest.TestCase):
    ''' Caso de teste da Browser View BarraHelper '''
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        pp = self.portal.portal_properties
        self.sheet = getattr(pp, 'brasil_gov', None)
        # Como nao eh um teste funcional, este objeto
        # REQUEST precisa ser anotado com o browser layer
        alsoProvides(self.portal.REQUEST, IBarraInstalada)

    def test_helper_view_registration(self):
        ''' Validamos se BarraHelper esta registrada '''
        view = self.portal.restrictedTraverse('@@barra_helper')
        view = view.__of__(self.portal)
        self.failUnless(view)

    def test_helper_view_local(self):
        ''' Uso do metodo local '''
        # Obtemos a Browser view
        view = self.portal.restrictedTraverse('@@barra_helper')
        # Validamos que ela retorne o valor padrao para
        # o metodo remoto(configurado em profiles/default/propertiestool.xml)
        self.assertFalse(view.local())
        # Alteramos o valor para hospedagem para local
        self.sheet.local = True
        # O resultado da consulta a Browser View deve se adequar
        self.assertTrue(view.local())


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
