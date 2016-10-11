# -*- coding: utf-8 -*-
""" Modulo que implementa uma browser view de suporte a Barra de Identidade"""
from Acquisition import aq_inner
from brasil.gov.barra.interfaces import IBarraHelper
from plone import api
from Products.Five import BrowserView
from zope.interface import implementer


@implementer(IBarraHelper)
class BarraHelper(BrowserView):
    """Browser view que retorna as configuracoes da Barra de Identidade"""

    def __init__(self, context, request, *args, **kwargs):
        """Inicializacao da browser view

            :param context: [requerido] Contexto que esta view e utilizada.
            :type context: objeto context
            :param request: [requerido] Request para o qual obteremos a view
            :type request: objeto request.
            :returns: Nothing
            :rtype: None
        """
        super(BarraHelper, self).__init__(context, request, *args, **kwargs)
        context = aq_inner(context)
        self.context = context
        # Obtem a tool portal_properties
        pp = api.portal.get_tool('portal_properties')
        # Armazena a property sheet brasil_gov no atributo sheet desta classe
        # Caso a sheet nao exista, retornamos None
        self.sheet = getattr(pp, 'brasil_gov', None)

    def local(self):
        """Retorna se a barra deve ser servida localmente

            :returns: Se devemos servir a barra localmente
            :rtype: bool
        """
        # Retorna se a barra sera montada localmente,
        # como armazenada na property sheet ou o valor padrao True
        local = True
        if self.sheet:
            local = self.sheet.getProperty('local', local)
        return local
