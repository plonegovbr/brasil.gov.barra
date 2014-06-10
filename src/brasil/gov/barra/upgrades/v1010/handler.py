# -*- coding: utf-8 -*-
from brasil.gov.barra.config import PROJECTNAME
from plone.app.upgrade.utils import loadMigrationProfile

import logging

logger = logging.getLogger(PROJECTNAME)


def apply_profile(context):
    """Atualiza perfil para versao 1010"""
    logger = logging.getLogger(PROJECTNAME)
    profile = 'profile-brasil.gov.barra.upgrades.v1010:default'
    loadMigrationProfile(context, profile)
    logger.info('Atualizado para versao 1010')
