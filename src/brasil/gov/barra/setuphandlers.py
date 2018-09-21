# -*- coding:utf-8 -*-
from Products.CMFPlone import interfaces as plone_interfaces
from Products.CMFQuickInstallerTool import interfaces as qi_interfaces
from zope.interface import implementer


@implementer(qi_interfaces.INonInstallable)
class HiddenProducts(object):  # pragma: no cover

    @staticmethod
    def getNonInstallableProducts():
        """Hide in the add-ons configlet."""
        return [
        ]


@implementer(plone_interfaces.INonInstallable)
class HiddenProfiles(object):  # pragma: no cover

    @staticmethod
    def getNonInstallableProfiles():
        """Hide at site creation."""
        return [
            'brasil.gov.barra:uninstall',
        ]
