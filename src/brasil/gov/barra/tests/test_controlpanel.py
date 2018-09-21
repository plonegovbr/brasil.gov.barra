# -*- coding: utf-8 -*-
from brasil.gov.barra.testing import INTEGRATION_TESTING
from plone import api
from plone.app.testing import logout

import unittest


class ControlPanelTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.controlpanel = self.portal['portal_controlpanel']

    def test_controlpanel_view(self):
        """Validamos se o control panel esta acessivel"""
        view = api.content.get_view(
            name='brasil.gov.barra-config',
            context=self.portal,
            request=self.portal.REQUEST,
        )
        view = view.__of__(self.portal)
        self.assertTrue(view())

    def test_controlpanel_configlet(self):
        """Acesso a view nao pode ser feito por usuario anonimo"""
        # Ao acessar a view como site administrator conseguimos acesso
        with api.env.adopt_roles(['Site Administrator']):
            # Listamos todas as acoes do painel de controle
            installed = [a['id'] for a in self.controlpanel.enumConfiglets(group='Products')]
            # Validamos que o painel de controle da barra esteja instalado
            self.assertTrue('barra-config' in installed)
        # Ao acessar a view como anonimo, a excecao e levantada
        with api.env.adopt_roles(['Anonymous']):
            # Listamos todas as acoes do painel de controle
            installed = [a['id'] for a in self.controlpanel.enumConfiglets(group='Products')]
            self.assertFalse('barra-config' in installed)

    def test_controlpanel_view_protected(self):
        """Acesso a view nao pode ser feito por usuario anonimo"""
        # Importamos a excecao esperada
        from AccessControl import Unauthorized
        # Deslogamos do portal
        logout()
        # Ao acessar a view como anonimo, a excecao e levantada
        with self.assertRaises(Unauthorized):
            self.portal.restrictedTraverse('@@brasil.gov.barra-config')

    def test_configlet_install(self):
        """Validamos se o control panel foi registrado"""
        # Listamos todas as acoes do painel de controle
        actions = [a.id for a in self.controlpanel.listActions()]
        # Validamos que o painel de controle da barra esteja instalado
        self.assertIn('barra-config', actions)

    def test_controlpanel_removed_on_uninstall(self):
        from brasil.gov.barra.config import PROJECTNAME
        qi = self.portal['portal_quickinstaller']

        with api.env.adopt_roles(['Manager']):
            qi.uninstallProducts(products=[PROJECTNAME])

        actions = [a.id for a in self.controlpanel.listActions()]
        self.assertNotIn('barra-config', actions)
