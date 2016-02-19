# -*- coding:utf-8 -*-
from brasil.gov.barra.config import PROJECTNAME
from plone import api

import logging


logger = logging.getLogger(PROJECTNAME)


def fix_css_references(setup_tool):
    """Fix css references after static files reorganization."""
    profile = 'profile-{0}:default'.format(PROJECTNAME)

    css_tool = api.portal.get_tool('portal_css')
    css_tool.renameResource(
        '++resource++brasil.gov.barra/css/main.css',
        '++resource++brasil.gov.barra/main.css',
    )
    logger.info('Updated css references.')
