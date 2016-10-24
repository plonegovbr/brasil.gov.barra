# -*- coding: utf-8 -*-
from brasil.gov.barra.config import PROJECTNAME
from brasil.gov.barra.upgrades import cook_css_resources
from plone.app.upgrade.utils import loadMigrationProfile

import logging


logger = logging.getLogger(PROJECTNAME)


def apply_profile(context):
    ''' Atualiza perfil para versao 1013 '''
    logger = logging.getLogger(PROJECTNAME)
    profile = 'profile-brasil.gov.barra.upgrades.v1013:default'
    loadMigrationProfile(context, profile)
    cook_css_resources(context)
    logger.info('CSS resources were cooked')
    logger.info('Atualizado para versao 1013')
