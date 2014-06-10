# -*- coding:utf-8 -*-
from Products.CMFPlone import interfaces as plone_interfaces
from Products.CMFQuickInstallerTool import interfaces as qi_interfaces
from zope.interface import implements

PROJECTNAME = "brasil.gov.barra"


class HiddenProducts(object):
    """Oculta produtos do QuickInstaller"""
    implements(qi_interfaces.INonInstallable)

    def getNonInstallableProducts(self):
        return [
            'brasil.gov.barra.upgrades.v1000',
            'brasil.gov.barra.upgrades.v1002',
            'brasil.gov.barra.upgrades.v1010',
        ]


class HiddenProfiles(object):
    """Oculta profiles da tela inicial de criacao do site"""
    implements(plone_interfaces.INonInstallable)

    def getNonInstallableProfiles(self):
        return [
            'brasil.gov.barra:uninstall',
            'brasil.gov.barra.upgrades.v1002:default'
            'brasil.gov.barra.upgrades.v1010:default'
        ]
