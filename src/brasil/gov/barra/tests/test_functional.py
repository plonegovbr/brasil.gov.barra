# -*- coding: utf-8 -*-
from brasil.gov.barra.testing import FUNCTIONAL_TESTING
from plone.testing import layered

import doctest
import unittest


optionflags = doctest.REPORT_ONLY_FIRST_FAILURE


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite('barra.txt',
                                     optionflags=optionflags),
                layer=FUNCTIONAL_TESTING),
        layered(doctest.DocFileSuite('painel.txt',
                                     optionflags=optionflags),
                layer=FUNCTIONAL_TESTING),
    ])
    return suite
