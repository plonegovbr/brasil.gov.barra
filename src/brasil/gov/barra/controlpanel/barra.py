# -*- coding:utf-8 -*-
""" Modulo que implementa o painel de controle da Barra de Identidade"""
from zope.schema import Bool
from zope.schema import Choice
from zope.component import adapts
from zope.interface import Interface
from zope.interface import implements

from zope.formlib.form import FormFields

from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFPlone.utils import getToolByName
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase

from plone.app.controlpanel.form import ControlPanelForm

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from brasil.gov.barra import MessageFactory as _

# Vocabulario das cores possiveis para a Barra de Identidade
cores = SimpleVocabulary([SimpleTerm(value=u'azul', title=_(u'Azul')),
                          SimpleTerm(value=u'cinza', title=_(u'Cinza')),
                          SimpleTerm(value=u'preto', title=_(u'Preto')),
                          SimpleTerm(value=u'verde', title=_(u'Verde'))])


class IBarraConfSchema(Interface):
    """ Schema de configuracao da Barra de Identidade """

    local = Bool(
        title=_(u'Usar barra local'),
        description=_(u'help_barra_local',
                      default=u"Devemos servir esta barra a partir "
                              u"deste site ou utilizar a versão "
                              u"disponível em barra.brasil.gov.br?"),
        required=False,
        default=True,
    )

    cor = Choice(
        title=_(u'Cor de fundo'),
        description=_(u'help_cor_barra',
                      default=u"Escolha uma das opções para "
                              u"cor de fundo da barra."),
        required=True,
        default=_(u'verde'),
        vocabulary=cores,
    )


class BarraControlPanelAdapter(SchemaAdapterBase):
    ''' Adapter para a raiz do site Plone suportar o schema
        de configuracao da barra de identidade
        Esta classe implementa uma maneira da raiz do site armazenar
        as configuracoes que serao geridas pelo painel de controle
    '''

    adapts(IPloneSiteRoot)
    implements(IBarraConfSchema)

    def __init__(self, context):
        super(BarraControlPanelAdapter, self).__init__(context)
        # Obtem a tool portal_properties
        portal_properties = getToolByName(context, 'portal_properties')
        # Define que o contexto a ser utilizado para o schema IBarraConfSchema
        # sera a property sheet brasil_gov
        self.context = portal_properties.brasil_gov

    # Define que o atributo local do schema sera armazenado como propriedade
    # dentro deste contexto
    local = ProxyFieldProperty(IBarraConfSchema['local'])

    # Define que o atributo cor do schema sera armazenado como propriedade
    # dentro deste contexto
    cor = ProxyFieldProperty(IBarraConfSchema['cor'])


class BarraControlPanel(ControlPanelForm):
    ''' Implementacao do painel de controle da Barra de Identidade '''
    # Define quais serao os campos a serem exibidos (IBarraConfSchema)
    form_fields = FormFields(IBarraConfSchema)

    # Define o titulo deste painel de controle
    label = _(u'Brasil.gov.br: Barra de identidade')
    # Define a descricao deste painel de controle
    description = _(u'Configurações do comportamento da barra de identidade')
    # Define o titulo do formulario deste painel de controle
    form_name = _(u'Configuração funcional e visual')
