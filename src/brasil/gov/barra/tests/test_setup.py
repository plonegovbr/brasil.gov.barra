# -*- coding: utf-8 -*-
from brasil.gov.barra.config import PROJECTNAME
from brasil.gov.barra.testing import INTEGRATION_TESTING
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.browserlayer.utils import registered_layers
from Products.GenericSetup.upgrade import listUpgradeSteps
from zope.site.hooks import setSite

import unittest2 as unittest


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
        css_barra = "++resource++brasil.gov.barra/css/main.css"
        self.assertTrue(css_barra in portal_css.getResourceIds(),
                        '%s not installed' % css_barra)

    def test_default_configuration(self):
        pp = self.portal.portal_properties
        sheet = getattr(pp, 'brasil_gov', None)
        self.assertTrue(sheet is not None)
        self.assertFalse(sheet.getProperty("local"))


class TestUpgrade(BaseTestCase):
    """ensure product upgrades work"""

    profile = 'brasil.gov.barra:default'

    def test_profile_version(self):
        # Testamos a versao do profile
        self.assertEquals(self.st.getLastVersionForProfile(self.profile),
                          (u'1002',))

    def test_to1000_from0(self):

        upgradeSteps = listUpgradeSteps(self.st,
                                        self.profile,
                                        '0.0')
        step = [step for step in upgradeSteps[0]
                if (step['dest'] == ('1000',))
                and (step['source'] == ('0', '0'))][0]
        step.get('step').doStep(self.st)

    def test_to1002_from1000(self):

        upgradeSteps = listUpgradeSteps(self.st,
                                        self.profile,
                                        '0.0')
        step = [step for step in upgradeSteps[1]
                if (step['dest'] == ('1002',))
                and (step['source'] == ('1000',))][0]
        step.get('step').doStep(self.st)


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
        css_barra = "++resource++brasil.gov.barra/css/main.css"
        self.assertTrue(css_barra not in portal_css.getResourceIds(),
                        '%s installed' % css_barra)
