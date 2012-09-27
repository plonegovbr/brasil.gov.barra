# -*- coding: utf-8 -*-

import unittest2 as unittest

from zope.site.hooks import setSite

from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login
from plone.app.testing import setRoles

from plone.browserlayer.utils import registered_layers

from brasil.gov.barra.config import PROJECTNAME
from brasil.gov.barra.testing import INTEGRATION_TESTING

STYLESHEETS = [
    "++resource++brasil.gov.barra/azul.css",
    "++resource++brasil.gov.barra/cinza.css",
    "++resource++brasil.gov.barra/preto.css",
    "++resource++brasil.gov.barra/verde.css",
]


class BaseTestCase(unittest.TestCase):
    """base test case to be used by other tests"""

    layer = INTEGRATION_TESTING

    def setUpUser(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager', 'Editor', 'Reviewer'])
        login(self.portal, TEST_USER_NAME)

    def setUp(self):
        portal = self.layer['portal']
        setSite(portal)
        self.portal = portal
        self.qi = getattr(self.portal, 'portal_quickinstaller')
        self.wt = getattr(self.portal, 'portal_workflow')
        self.st = getattr(self.portal, 'portal_setup')
        self.setUpUser()


class TestInstall(BaseTestCase):
    """ensure product is properly installed"""

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME),
                        '%s not installed' % PROJECTNAME)

    def test_browserlayer(self):
        from brasil.gov.barra.interfaces import IBarraInstalada
        self.assertTrue(IBarraInstalada in registered_layers())

    def test_cssregistry(self):
        portal_css = self.portal.portal_css
        for js in STYLESHEETS:
            self.assertTrue(js in portal_css.getResourceIds(),
                            '%s not installed' % js)

    def test_default_configuration(self):
        pp = self.portal.portal_properties
        sheet = getattr(pp, 'brasil_gov', None)
        self.assertTrue(sheet is not None)
        self.assertTrue(sheet.getProperty("cor") == 'verde')
        self.assertTrue(sheet.getProperty("local"))


class TestUninstall(BaseTestCase):
    """ensure product is properly uninstalled"""

    def setUp(self):
        BaseTestCase.setUp(self)
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

    def test_browserlayer(self):
        from brasil.gov.barra.interfaces import IBarraInstalada
        self.assertTrue(IBarraInstalada not in registered_layers())

    def test_cssregistry(self):
        portal_css = self.portal.portal_css
        for js in STYLESHEETS:
            self.assertTrue(js not in portal_css.getResourceIds(),
                            '%s installed' % js)
