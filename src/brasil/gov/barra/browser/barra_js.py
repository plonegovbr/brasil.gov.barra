# -*- coding: utf-8 -*-

from plone import api
from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class BarraViewlet(ViewletBase):
    """
    Viewlet que faz a chamada pura para o javascript externo do ministério do
    planejamento.

    Se o usuário marcar a opção para usar barra local, não renderiza a chamada
    javascript.
    """
    # Indica qual o template sera usado por este viewlet
    index = ViewPageTemplateFile('templates/barra_js.pt')

    def render(self):
        portal = api.portal.get()
        helper = api.content.get_view(
            name='barra_helper',
            context=portal,
            request=self.request,
        )

        if helper.local():
            return ''
        else:
            return super(BarraViewlet, self).render()
