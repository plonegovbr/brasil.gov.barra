# -*- coding:utf-8 -*-
from Products.CMFPlone import interfaces as plone_interfaces
from Products.CMFQuickInstallerTool import interfaces as qi_interfaces
from zope.interface import implementer

PROJECTNAME = 'brasil.gov.barra'


@implementer(qi_interfaces.INonInstallable)
class HiddenProducts(object):
    """Oculta produtos do QuickInstaller"""

    def getNonInstallableProducts(self):
        return [
            'brasil.gov.barra.upgrades.v1000',
            'brasil.gov.barra.upgrades.v1002',
            'brasil.gov.barra.upgrades.v1010',
        ]


@implementer(plone_interfaces.INonInstallable)
class HiddenProfiles(object):
    """Oculta profiles da tela inicial de criacao do site"""

    def getNonInstallableProfiles(self):
        return [
            'brasil.gov.barra:uninstall',
            'brasil.gov.barra.upgrades.v1002:default'
            'brasil.gov.barra.upgrades.v1010:default'
        ]
