# -*- coding: utf-8 -*-
from brasil.gov.barra.config import PROJECTNAME
from brasil.gov.barra.testing import INTEGRATION_TESTING
from plone import api
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.browserlayer.utils import registered_layers

import unittest


class BaseTestCase(unittest.TestCase):
    """base test case to be used by other tests"""

    layer = INTEGRATION_TESTING

    def setUpUser(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager', 'Editor', 'Reviewer'])
        login(self.portal, TEST_USER_NAME)

    def setUp(self):
        portal = self.layer['portal']
        self.portal = portal
        self.qi = api.portal.get_tool('portal_quickinstaller')
        self.wt = api.portal.get_tool('portal_workflow')
        self.st = api.portal.get_tool('portal_setup')
        self.setUpUser()


class TestInstall(BaseTestCase):
    """ensure product is properly installed"""

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME),
                        '{0} not installed'.format(PROJECTNAME))

    def test_browserlayer(self):
        from brasil.gov.barra.interfaces import IBarraInstalada
        self.assertIn(IBarraInstalada, registered_layers())

    def test_default_configuration(self):
        pp = api.portal.get_tool('portal_properties')
        sheet = getattr(pp, 'brasil_gov', None)
        self.assertIsNotNone(sheet)
        self.assertFalse(sheet.getProperty('local'))

    def test_profile_version(self):
        profile = 'brasil.gov.barra:default'
        self.assertEqual(
            self.st.getLastVersionForProfile(profile), (u'2000',))


class TestUninstall(BaseTestCase):
    """ensure product is properly uninstalled"""

    def setUp(self):
        BaseTestCase.setUp(self)
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

    def test_browserlayer(self):
        from brasil.gov.barra.interfaces import IBarraInstalada
        self.assertNotIn(IBarraInstalada, registered_layers())
