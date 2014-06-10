# -*- coding: utf-8 -*-
""" Modulo que implementa o(s) viewlet(s) da Barra de Identidade"""
from plone import api
from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class BarraViewlet(ViewletBase):
    """Implementacao do viewlet da Barra de Identidade do Governo
       Este viewlet eh registrado como no arquivo browser/configure.zcml
       e habilitado no arquivo profiles/default/viewlets.xml
    """
    # Indica qual o template sera usado por este viewlet
    index = ViewPageTemplateFile('templates/barra.pt')

    def update(self):
        """Prepara/Atualiza os valores utilizados pelo Viewlet"""
        super(BarraViewlet, self).update()
        # Disponibiliza uma variavel site_url que retorna a raiz do
        # site Plone. No template ela pode ser chamada como view/site_url
        portal = api.portal.get()
        helper = api.content.get_view(
            name='barra_helper',
            context=portal,
            request=self.request,
        )
        self.local = helper.local
        self.site_url = portal.absolute_url()
