# -*- coding:utf-8 -*-
from brasil.gov.barra.config import PROJECTNAME
from plone import api

import logging


logger = logging.getLogger(PROJECTNAME)


def cook_css_resources(context):  # pragma: no cover
    """Cook CSS resources."""
    css_tool = api.portal.get_tool('portal_css')
    css_tool.cookResources()
    logger.info('CSS resources were cooked')
