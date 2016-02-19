# -*- coding: utf-8 -*-
from brasil.gov.barra.interfaces import IBarraInstalada
from brasil.gov.barra.testing import INTEGRATION_TESTING
from plone import api
from plone.app.testing import logout
from zope.interface import alsoProvides

import unittest as unittest


class ControlPanelTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        # Como nao eh um teste funcional, este objeto
        # REQUEST precisa ser anotado com o browser layer
        alsoProvides(self.portal.REQUEST, IBarraInstalada)

    def test_controlpanel_view(self):
        """Validamos se o control panel esta acessivel"""
        view = api.content.get_view(
            name='brasil.gov.barra-config',
            context=self.portal,
            request=self.portal.REQUEST,
        )
        view = view.__of__(self.portal)
        self.failUnless(view())

    def test_controlpanel_configlet(self):
        """Acesso a view nao pode ser feito por usuario anonimo"""
        controlpanel = api.portal.get_tool('portal_controlpanel')
        # Ao acessar a view como site administrator conseguimos acesso
        with api.env.adopt_roles(['Site Administrator', ]):
            # Listamos todas as acoes do painel de controle
            installed = [a['id'] for a in controlpanel.enumConfiglets(group='Products')]
            # Validamos que o painel de controle da barra esteja instalado
            self.failUnless('barra-config' in installed)
        # Ao acessar a view como anonimo, a excecao e levantada
        with api.env.adopt_roles(['Anonymous', ]):
            # Listamos todas as acoes do painel de controle
            installed = [a['id'] for a in controlpanel.enumConfiglets(group='Products')]
            self.failIf('barra-config' in installed)

    def test_controlpanel_view_protected(self):
        """Acesso a view nao pode ser feito por usuario anonimo"""
        # Importamos a excecao esperada
        from AccessControl import Unauthorized
        # Deslogamos do portal
        logout()
        # Ao acessar a view como anonimo, a excecao e levantada
        self.assertRaises(Unauthorized, self.portal.restrictedTraverse,
                          '@@brasil.gov.barra-config')

    def test_configlet_install(self):
        """Validamos se o control panel foi registrado"""
        # Obtemos a ferramenta de painel de controle
        controlpanel = api.portal.get_tool('portal_controlpanel')
        # Listamos todas as acoes do painel de controle
        installed = [a.getAction(self)['id']
                     for a in controlpanel.listActions()]
        # Validamos que o painel de controle da barra esteja instalado
        self.failUnless('barra-config' in installed)
