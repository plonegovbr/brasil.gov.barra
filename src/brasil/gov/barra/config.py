# -*- coding:utf-8 -*-
from Products.CMFPlone import interfaces as plone_interfaces
from Products.CMFQuickInstallerTool import interfaces as qi_interfaces
from zope.interface import implementer

import os


BARRA_JS_STATIC_FILE_LOCATION = os.path.join(
    os.path.dirname(__file__), 'static')

PROJECTNAME = 'brasil.gov.barra'


@implementer(qi_interfaces.INonInstallable)
class HiddenProducts(object):
    """Oculta produtos do QuickInstaller"""

    def getNonInstallableProducts(self):
        return [
        ]


@implementer(plone_interfaces.INonInstallable)
class HiddenProfiles(object):
    """Oculta profiles da tela inicial de criacao do site"""

    def getNonInstallableProfiles(self):
        return [
            'brasil.gov.barra:uninstall',
        ]
