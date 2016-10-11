# -*- coding:utf-8 -*-
""" Modulo que implementa o painel de controle da Barra de Identidade"""
from brasil.gov.barra import MessageFactory as _
from plone import api
from plone.app.controlpanel.form import ControlPanelForm
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from zope.component import adapter
from zope.formlib.form import FormFields
from zope.interface import implementer
from zope.interface import Interface
from zope.schema import Bool


class IBarraConfSchema(Interface):
    """Schema de configuracao da Barra de Identidade"""

    local = Bool(
        title=_(u'Usar barra local'),
        description=_(u'help_barra_local',
                      default=u'Devemos servir esta barra a partir '
                              u'deste site ou utilizar a versão '
                              u'disponível em barra.brasil.gov.br?'),
        required=False,
        default=True,
    )


@adapter(IPloneSiteRoot)
@implementer(IBarraConfSchema)
class BarraControlPanelAdapter(SchemaAdapterBase):
    """Adapter para a raiz do site Plone suportar o schema
       de configuracao da barra de identidade
       Esta classe implementa uma maneira da raiz do site armazenar
       as configuracoes que serao geridas pelo painel de controle
    """

    def __init__(self, context):
        super(BarraControlPanelAdapter, self).__init__(context)
        # Obtem a tool portal_properties
        portal_properties = api.portal.get_tool('portal_properties')
        # Define que o contexto a ser utilizado para o schema IBarraConfSchema
        # sera a property sheet brasil_gov
        self.context = portal_properties.brasil_gov

    # Define que o atributo local do schema sera armazenado como propriedade
    # dentro deste contexto
    local = ProxyFieldProperty(IBarraConfSchema['local'])


class BarraControlPanel(ControlPanelForm):
    """Implementacao do painel de controle da Barra de Identidade"""
    # Define quais serao os campos a serem exibidos (IBarraConfSchema)
    form_fields = FormFields(IBarraConfSchema)

    # Define o titulo deste painel de controle
    label = _(u'Brasil.gov.br: Barra de identidade')
    # Define a descricao deste painel de controle
    description = _(u'Configurações do comportamento da barra de identidade')
    # Define o titulo do formulario deste painel de controle
    form_name = _(u'Configuração funcional e visual')
