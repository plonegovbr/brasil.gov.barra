# -*- coding:utf-8 -*-
from zope.interface import Interface


class IBarraInstalada(Interface):
    """Layer especifico para este add-on

    Esta interface e referenciada em browserlayers.xml.

    Views e viewlets registrados para este layer serao exibidos
    apenas quando o produto estiver instalado
    """


class IBarraHelper(Interface):
    """Interface da Browser View BarraHelper
       Os metodos definidos aqui serao acessiveis
       diretamente na Browser View
    """
    def local():
        """Barra servida localmente"""
