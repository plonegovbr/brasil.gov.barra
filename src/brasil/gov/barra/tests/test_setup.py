# -*- coding: utf-8 -*-
from brasil.gov.barra.config import PROJECTNAME
from brasil.gov.barra.testing import INTEGRATION_TESTING
from plone import api
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.browserlayer.utils import registered_layers
from Products.GenericSetup.upgrade import listUpgradeSteps
from zope.site.hooks import setSite

import unittest as unittest


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
        self.qi = api.portal.get_tool('portal_quickinstaller')
        self.wt = api.portal.get_tool('portal_workflow')
        self.st = api.portal.get_tool('portal_setup')
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
        portal_css = api.portal.get_tool('portal_css')
        css_barra = "++resource++brasil.gov.barra/main.css"
        self.assertTrue(css_barra in portal_css.getResourceIds(),
                        '%s not installed' % css_barra)

    def test_default_configuration(self):
        pp = api.portal.get_tool('portal_properties')
        sheet = getattr(pp, 'brasil_gov', None)
        self.assertTrue(sheet is not None)
        self.assertFalse(sheet.getProperty("local"))


class TestUpgrade(BaseTestCase):
    """ensure product upgrades work"""

    profile = 'brasil.gov.barra:default'

    def test_profile_version(self):
        # Testamos a versao do profile
        self.assertEqual(
            self.st.getLastVersionForProfile(self.profile),
            (u'1012',)
        )

    def _executa_atualizacao(self, source, dest):
        upgradeSteps = listUpgradeSteps(self.st,
                                        self.profile,
                                        source)
        if source == '0.0':
            source = ('0', '0')
        else:
            source = (source, )
        step = [step for step in upgradeSteps[0]
                if (step['dest'] == (dest,)) and (step['source'] == source)][0]
        step.get('step').doStep(self.st)

    def test_to1000_from0(self):
        self._executa_atualizacao('0.0', '1000')

    def test_to1002_from1000(self):
        css_id = '++resource++brasil.gov.barra/preto.css'
        css_tool = api.portal.get_tool('portal_css')
        css_tool.registerResource(
            css_id,
            enabled=1,
            cookable=False,
            cacheable=False
        )
        self._executa_atualizacao('1000', '1002')
        self.assertNotIn(
            css_id,
            css_tool.getResourceIds()
        )

    def test_to1002_from1010(self):
        self._executa_atualizacao('1002', '1010')
        controlpanel = api.portal.get_tool('portal_controlpanel')
        with api.env.adopt_roles(['Site Administrator', ]):
            # Listamos todas as acoes do painel de controle
            installed = [a['id'] for a in controlpanel.enumConfiglets(group='Products')]
            # Validamos que o painel de controle da barra esteja instalado
            self.failUnless('barra-config' in installed)


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
        css_barra = "++resource++brasil.gov.barra/main.css"
        self.assertTrue(css_barra not in portal_css.getResourceIds(),
                        '%s installed' % css_barra)
