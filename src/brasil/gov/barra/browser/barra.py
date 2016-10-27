# -*- coding: utf-8 -*-
""" Modulo que implementa o(s) viewlet(s) da Barra de Identidade"""
from plone import api
from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class BarraViewletJs(ViewletBase):
    """
    Viewlet que faz a chamada para o javascript da barra do Ministério do
    Planejamento.

    Se o usuário marcar a opção para usar barra local, utiliza um barra.js que
    está no pacote.
    """
    # Indica qual o template sera usado por este viewlet
    index = ViewPageTemplateFile('templates/barra_js.pt')

    def update(self):
        """Prepara/Atualiza os valores utilizados pelo Viewlet"""
        super(BarraViewletJs, self).update()
        portal = api.portal.get()
        helper = api.content.get_view(
            name='barra_helper',
            context=portal,
            request=self.request,
        )
        self.local = helper.local
