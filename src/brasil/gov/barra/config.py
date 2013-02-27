# -*- coding:utf-8 -*-
from Products.CMFPlone import interfaces as plone_interfaces
from zope.interface import implements

PROJECTNAME = "brasil.gov.barra"


class HiddenProfiles(object):
    implements(plone_interfaces.INonInstallable)

    def getNonInstallableProfiles(self):
        return [u'brasil.gov.barra:uninstall']
