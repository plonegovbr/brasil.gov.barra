# -*- coding: utf-8 -*-
from brasil.gov.barra.config import PROJECTNAME
from plone.app.upgrade.utils import loadMigrationProfile
from Products.CMFCore.utils import getToolByName

import logging


logger = logging.getLogger(PROJECTNAME)


def unregister_old_css(context):
    """ Desregistra css utilizado antigamente
    """
    CSS_TO_REMOVE = [
        '++resource++brasil.gov.barra/azul.css',
        '++resource++brasil.gov.barra/verde.css',
        '++resource++brasil.gov.barra/cinza.css',
        '++resource++brasil.gov.barra/preto.css'
    ]
    css_tool = getToolByName(context, 'portal_css')
    for css in CSS_TO_REMOVE:
        if css in css_tool.getResourceIds():
            css_tool.unregisterResource(css)
            logger.info('"{0}"" resource was removed'.format(css))
            css_tool.cookResources()
            logger.info('CSS resources were cooked')
        else:
            logger.debug('"{0}" resource not found in portal_css'.format(css))


def apply_profile(context):
    ''' Atualiza perfil para versao 1002 '''
    logger = logging.getLogger(PROJECTNAME)
    profile = 'profile-brasil.gov.barra.upgrades.v1002:default'
    loadMigrationProfile(context, profile)
    unregister_old_css(context)
    logger.info('Atualizado para versao 1002')
