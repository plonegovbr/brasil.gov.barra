# -*- coding: utf-8 -*-
from brasil.gov.barra.config import PROJECTNAME
from brasil.gov.barra.interfaces import IBarraInstalada
from brasil.gov.barra.testing import INTEGRATION_TESTING
from plone.browserlayer.utils import registered_layers

import unittest


class TestInstall(unittest.TestCase):
    """Ensure product is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installed(self):
        qi = self.portal['portal_quickinstaller']
        self.assertTrue(qi.isProductInstalled(PROJECTNAME))

    def test_browserlayer(self):
        self.assertIn(IBarraInstalada, registered_layers())

    def test_default_configuration(self):
        pp = self.portal['portal_properties']
        sheet = getattr(pp, 'brasil_gov', None)
        self.assertIsNotNone(sheet)
        self.assertFalse(sheet.getProperty('local'))

    def test_profile_version(self):
        setup_tool = self.portal['portal_setup']
        profile = 'brasil.gov.barra:default'
        self.assertEqual(
            setup_tool.getLastVersionForProfile(profile), (u'2000',))


class TestUninstall(unittest.TestCase):
    """Ensure product is properly uninstalled."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

    def test_browserlayer_removed(self):
        self.assertNotIn(IBarraInstalada, registered_layers())
